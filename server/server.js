const express = require('express');
const cors = require('cors');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3001;

// Middleware
app.use(cors());
app.use(express.json());

// Serve static files from parent directory (the game)
app.use(express.static(path.join(__dirname, '..')));

// Data file path - use persistent disk on Render, local otherwise
const DATA_DIR = process.env.DATA_PATH || __dirname;
const DATA_FILE = path.join(DATA_DIR, 'leaderboard.json');

// Initialize data file if it doesn't exist
function initDataFile() {
    if (!fs.existsSync(DATA_FILE)) {
        fs.writeFileSync(DATA_FILE, JSON.stringify({ scores: [] }, null, 2));
    }
}

function readScores() {
    try {
        initDataFile();
        const data = JSON.parse(fs.readFileSync(DATA_FILE, 'utf8'));
        return data.scores || [];
    } catch (error) {
        console.error('Error reading scores:', error);
        return [];
    }
}

function writeScores(scores) {
    try {
        fs.writeFileSync(DATA_FILE, JSON.stringify({ scores }, null, 2));
        return true;
    } catch (error) {
        console.error('Error writing scores:', error);
        return false;
    }
}

// API Routes

// Get top scores (global leaderboard)
app.get('/api/leaderboard', (req, res) => {
    try {
        const limit = Math.min(parseInt(req.query.limit) || 10, 100);
        const scores = readScores()
            .sort((a, b) => b.score - a.score || a.cards_played - b.cards_played)
            .slice(0, limit);

        res.json({ success: true, scores });
    } catch (error) {
        console.error('Error fetching leaderboard:', error);
        res.status(500).json({ success: false, error: 'Failed to fetch leaderboard' });
    }
});

// Submit a new score
app.post('/api/leaderboard', (req, res) => {
    try {
        const { name, score, cardsPlayed, finalEra, won } = req.body;

        // Validation
        if (!name || typeof name !== 'string' || name.trim().length === 0) {
            return res.status(400).json({ success: false, error: 'Name is required' });
        }
        if (typeof score !== 'number' || score < 0) {
            return res.status(400).json({ success: false, error: 'Valid score is required' });
        }

        const sanitizedName = name.trim().substring(0, 50);
        const newEntry = {
            id: Date.now(),
            name: sanitizedName,
            score: Math.floor(score),
            cards_played: cardsPlayed || 0,
            final_era: finalEra || 'unknown',
            won: won ? 1 : 0,
            created_at: new Date().toISOString()
        };

        const scores = readScores();
        scores.push(newEntry);

        // Keep top 100 scores
        scores.sort((a, b) => b.score - a.score || a.cards_played - b.cards_played);
        const trimmedScores = scores.slice(0, 100);

        writeScores(trimmedScores);

        // Calculate rank
        const rank = trimmedScores.findIndex(s => s.id === newEntry.id) + 1;

        res.json({
            success: true,
            id: newEntry.id,
            rank: rank
        });
    } catch (error) {
        console.error('Error submitting score:', error);
        res.status(500).json({ success: false, error: 'Failed to submit score' });
    }
});

// Get stats
app.get('/api/stats', (req, res) => {
    try {
        const scores = readScores();
        const stats = {
            total_games: scores.length,
            total_wins: scores.filter(s => s.won).length,
            avg_score: scores.length > 0 ? Math.round(scores.reduce((a, b) => a + b.score, 0) / scores.length) : 0,
            high_score: scores.length > 0 ? Math.max(...scores.map(s => s.score)) : 0
        };

        res.json({ success: true, stats });
    } catch (error) {
        console.error('Error fetching stats:', error);
        res.status(500).json({ success: false, error: 'Failed to fetch stats' });
    }
});

// Health check for Render
app.get('/api/health', (req, res) => {
    res.json({ status: 'ok', timestamp: new Date().toISOString() });
});

// Start server
app.listen(PORT, () => {
    console.log(`Equilibrium Leaderboard API running on port ${PORT}`);
    console.log(`Data file: ${DATA_FILE}`);
    initDataFile();
});
