# Equilibrium: A Durkheim Solidarity Game

A Reigns-style educational game that teaches Émile Durkheim's concepts of mechanical solidarity, organic solidarity, and anomie through interactive gameplay.

## Overview

Students guide a society through "the great transition" from mechanical to organic solidarity—the central narrative of Durkheim's *Division of Labor in Society*. Through binary choices presented on cards, players must balance four interconnected social forces while avoiding societal collapse.

**Play online:** [Coming soon]

## Learning Objectives

After playing Equilibrium, students will be able to:

1. **Distinguish mechanical from organic solidarity** - Understanding that social cohesion can be based on similarity (mechanical) or interdependence (organic)

2. **Explain anomie as structural, not moral** - Recognizing that normlessness emerges from misalignment between social change and moral regulation, not from individual failings

3. **Analyze the risks of rapid modernization** - Experiencing how the division of labor can outpace the development of new integrative institutions

4. **Understand the role of occupational groups** - Seeing how professional associations can stabilize modern societies

## Game Mechanics

### The Four Meters

| Meter | Durkheim Concept | What It Represents |
|-------|------------------|-------------------|
| **Social Cohesion** | Collective conscience / Solidarity | The bonds holding society together |
| **Division of Labor** | Specialization | Economic complexity and interdependence |
| **Moral Regulation** | Normative framework | Rules, institutions, and their legitimacy |
| **Social Differentiation** | Individualism | Diversity of roles and identities |

### Eras

The game progresses through three eras (one-way progression):

1. **Traditional Era** (Mechanical Solidarity)
   - Unity through similarity
   - Repressive law dominates
   - Collective conscience is strong

2. **Transitional Era** (The Danger Zone)
   - Old bonds weaken, new ones forming
   - Anomie risk is highest
   - Key teaching moment for Durkheim's theory

3. **Modern Era** (Organic Solidarity)
   - Unity through interdependence
   - Restitutive law dominates
   - Professional ethics regulate economic life

### Win Condition

Reach Year 100 with:
- High division of labor (specialization achieved)
- Maintained social cohesion (new bonds replaced old)
- Stable moral regulation (norms adapted to change)
- No active anomie

### Collapse Conditions

Each era has distinct ways to fail, all drawn from Durkheim:

**Traditional Era:**
- Collective Conscience Dissolved
- Repression Devoured Its Own
- Society Became Its Own Museum

**Transitional Era:**
- Sustained Anomie
- The Bonds Broke Before New Ones Formed
- Forced Division of Labor

**Modern Era:**
- Anomic Division of Labor
- The Worker Becomes a Cog
- Interdependence Without Integration

## Durkheimian Mechanics

The game implements several mechanics that directly model Durkheim's insights:

### 1. Legitimacy Inertia
Moral regulation changes slowly—60% of effects apply immediately, 40% resolves over subsequent turns. This teaches that new institutions need time to develop authority.

### 2. Innovation Scaling
Differentiation gains are reduced when solidarity and legitimacy are low. This models Durkheim's insight that differentiation without integration accelerates anomie.

### 3. Anomie Countdown
Anomie is corrosive, not instantly fatal. Players can survive several turns in anomie, teaching that instability can be managed but not ignored.

### 4. Occupational Density
A hidden variable tracks when specialization rises alongside maintained solidarity, providing anomie resistance—modeling Durkheim's emphasis on professional groups.

### 5. Era-Specific Law Effects
- **Traditional:** High legitimacy boosts solidarity (repressive law binds community)
- **Modern:** High legitimacy boosts productivity (contract law enables exchange)

## Classroom Use

### Before Playing
- Introduce Durkheim's basic concepts (10-15 min)
- Explain the difference between mechanical and organic solidarity
- Define anomie as "normlessness during rapid change"

### During Play
- Have students play individually or in pairs (15-20 min)
- Encourage discussion of choices: "Why did you pick that?"
- Note which era students find most difficult

### After Playing (Discussion Questions)

1. **On Solidarity Types:**
   - "What held your society together in the Traditional Era vs. the Modern Era?"
   - "Did high specialization automatically create organic solidarity? Why not?"

2. **On Anomie:**
   - "When did you feel most unstable? What was happening to the meters?"
   - "How is anomie different from simply having low solidarity?"

3. **On the Transition:**
   - "What made the Transitional Era dangerous?"
   - "What strategies helped you survive the transition?"

4. **On Contemporary Society:**
   - "Where do you see anomie in modern society?"
   - "What institutions play the role of 'occupational groups' today?"

### Assessment Ideas

- **Reflection Essay:** "Describe your society's collapse using Durkheim's concepts"
- **Comparative Analysis:** "How does the game's model of anomie compare to Durkheim's original theory?"
- **Strategy Guide:** "Write advice for new players using only Durkheimian terminology"

## Installation

### Local Development

```bash
# Clone the repository
git clone https://github.com/nealcaren/equilibrium.git
cd equilibrium

# Install server dependencies
cd server
npm install

# Start the server
npm start

# Open http://localhost:3001 in your browser
```

### Deployment (Render)

The repository includes a `render.yaml` for easy deployment:

1. Fork this repository
2. Connect to [Render](https://render.com)
3. Create a new Blueprint and select your fork
4. Render will auto-detect the configuration

## Project Structure

```
equilibrium/
├── index.html          # Main game (single-page app)
├── cards.json          # Original scenario cards
├── new-cards.json      # Additional scenario cards
├── CARD_GUIDE.md       # Guide for creating new cards
├── server/
│   ├── package.json
│   └── server.js       # Express server with leaderboard API
└── render.yaml         # Render deployment config
```

## Creating New Cards

See [CARD_GUIDE.md](CARD_GUIDE.md) for detailed instructions on creating scenario cards. Cards are organized by era:

- **Traditional:** Village elders, clan patriarchs, guild masters
- **Transitional:** Factory owners, reformers, union organizers
- **Modern:** Tech executives, data scientists, platform workers
- **Universal:** Policy dilemmas that work in any era

### Card Balance Guidelines

- Both choices should have trade-offs (no "right answers")
- Effects should make thematic sense for Durkheim's theory
- Typical effect ranges: ±5 (minor) to ±25 (transformative)

## Theoretical Background

This game is based on Émile Durkheim's *The Division of Labor in Society* (1893). Key concepts:

- **Mechanical Solidarity:** Social cohesion based on similarity and shared collective conscience
- **Organic Solidarity:** Social cohesion based on functional interdependence and complementary differences
- **Anomie:** A state of normlessness that occurs when social change outpaces moral regulation
- **Collective Conscience:** The totality of beliefs and sentiments common to members of a society
- **Division of Labor:** Not merely economic, but the primary driver of social evolution

## Win Rate

In automated testing, the game has approximately a **20% win rate** with optimized strategy. Most failures occur in the Modern Era from hyper-specialization ("The Worker Becomes a Cog"). This difficulty is intentional—Durkheim himself noted that achieving healthy organic solidarity is challenging.

## Credits

- Game concept and design: Neal Caren
- Theoretical foundation: Émile Durkheim
- Built with: HTML, JavaScript, Tailwind CSS, Node.js

## License

MIT License - Feel free to use, modify, and adapt for educational purposes.

## Contributing

Contributions welcome! Particularly:
- New scenario cards (see CARD_GUIDE.md)
- Translations
- Accessibility improvements
- Balance adjustments based on classroom testing

---

*"Man is only a moral being because he lives in society. Let social life disappear, and moral life would disappear with it."* — Émile Durkheim
