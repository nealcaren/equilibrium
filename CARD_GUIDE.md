# Card Creation Guide for Equilibrium

This guide explains how to create new scenario cards for the Durkheim solidarity game.

## Card Structure

Each card is a JSON object with this structure:

```json
{
  "character": "Village Elder",
  "text": "The harvest festival has always united our community. Some young people want to skip the rituals and focus on trade instead.",
  "choiceA": {
    "text": "Preserve the festival",
    "effects": { "solidarity": 15, "productivity": -10, "legitimacy": 10, "innovation": -10 }
  },
  "choiceB": {
    "text": "Allow individual choice",
    "effects": { "solidarity": -15, "productivity": 10, "legitimacy": -5, "innovation": 10 }
  }
}
```

### Fields

| Field | Description |
|-------|-------------|
| `character` | Who is presenting this dilemma (keep it short: 2-4 words) |
| `text` | The scenario description (2-3 sentences, ~150-200 characters ideal) |
| `choiceA.text` | Left button label (2-5 words) |
| `choiceB.text` | Right button label (2-5 words) |
| `effects` | How each choice changes the four meters |

## The Four Meters

| Meter | JSON key | What it represents | Durkheim connection |
|-------|----------|-------------------|---------------------|
| **Social Cohesion** | `solidarity` | Bonds holding society together | Transforms from similarity-based (mechanical) to interdependence-based (organic) |
| **Division of Labor** | `productivity` | Specialization, economic complexity | Primary driver of organic solidarity |
| **Moral Regulation** | `legitimacy` | Norms, rules, institutional trust | When this lags behind change, anomie results |
| **Social Differentiation** | `innovation` | Individual difference, diversity | Increases with modernization |

### Key Insight for Card Design
The challenge is that organic solidarity requires BOTH high division of labor AND maintained cohesion. Cards that boost productivity/innovation while destroying solidarity lead to anomie, not progress.

## Effect Guidelines

### Typical Effect Ranges

- **Small effect**: ±5 to ±10 (minor policy tweak)
- **Medium effect**: ±10 to ±20 (significant change)
- **Large effect**: ±20 to ±30 (transformative decision)

### Balance Rules

1. **No free lunches**: Every choice should have trade-offs
2. **Net zero-ish**: Total effects across both choices should roughly balance
3. **Thematic consistency**: Effects should make logical sense for the scenario

### Common Patterns

**Modernization trade-off** (traditional → modern):
- Choice A: +solidarity, -productivity, +legitimacy, -innovation
- Choice B: -solidarity, +productivity, -legitimacy, +innovation

**Liberty vs. security**:
- Choice A: -solidarity, +productivity, -legitimacy, +innovation
- Choice B: +solidarity, -productivity, +legitimacy, -innovation

**Elite vs. populist**:
- Choice A: -solidarity, +productivity, +legitimacy, +innovation
- Choice B: +solidarity, -productivity, -legitimacy, -innovation

## Era Categories

Place your card in the appropriate era array in `cards.json`:

### `traditional` - Mechanical Solidarity Era
Cards should feel pre-industrial, community-based:
- Village/clan/tribe settings
- Religious or customary authority
- Communal resources and decision-making
- Oral traditions, apprenticeships
- Characters: elders, priests, guild masters, clan leaders

**Example themes**: harvest festivals, arranged marriages, communal land, craft guilds, sacred laws

### `transitional` - The Great Transformation
Cards about industrialization and social upheaval:
- Factories, railroads, urbanization
- New institutions (banks, schools, professional bodies)
- Old vs. new tensions
- Characters: factory owners, reformers, union organizers, city planners

**Example themes**: factory labor, public education, railroad expansion, labor unions, standardized time

### `modern` - Organic Solidarity Era
Cards about contemporary/future society:
- Technology and digital life
- Global interconnection
- Highly specialized roles
- Characters: tech executives, data scientists, platform workers, AI researchers

**Example themes**: AI governance, gig economy, social media, genetic engineering, remote work

### `universal` - Any Era
Policy dilemmas that work regardless of time period:
- Healthcare, education, trade
- Immigration, taxation, environment
- Justice and punishment

## Writing Good Cards

### Do:
- Present genuine dilemmas (both choices have merit)
- Connect to Durkheim's concepts implicitly
- Use specific, concrete scenarios
- Make the stakes clear
- Keep text concise

### Don't:
- Make one choice obviously "correct"
- Use modern jargon in traditional cards
- Create scenarios with no real trade-off
- Write walls of text
- Be preachy or didactic

## Examples by Era

### Traditional Era Card
```json
{
  "character": "Clan Patriarch",
  "text": "Land has always been held communally by the clan. Some families want individual ownership to improve their plots.",
  "choiceA": {
    "text": "Maintain communal land",
    "effects": { "solidarity": 20, "productivity": -15, "legitimacy": 10, "innovation": -10 }
  },
  "choiceB": {
    "text": "Allow private ownership",
    "effects": { "solidarity": -25, "productivity": 20, "legitimacy": -15, "innovation": 15 }
  }
}
```
*Why it works*: Enclosure of the commons is a classic mechanical → organic transition. Both choices have clear logic.

### Transitional Era Card
```json
{
  "character": "Labor Organizer",
  "text": "Factory workers are forming unions to protect their interests. This is a new form of association based on occupation, not family or village.",
  "choiceA": {
    "text": "Recognize unions",
    "effects": { "solidarity": 10, "productivity": -10, "legitimacy": 10, "innovation": 10 }
  },
  "choiceB": {
    "text": "Ban worker associations",
    "effects": { "solidarity": -15, "productivity": 15, "legitimacy": -15, "innovation": -5 }
  }
}
```
*Why it works*: Unions represent new organic solidarity (occupational groups). The text explicitly notes this shift.

### Modern Era Card
```json
{
  "character": "Remote Work Advocate",
  "text": "Workers want to work from home permanently. This offers flexibility but may erode workplace community and mentorship.",
  "choiceA": {
    "text": "Embrace remote work",
    "effects": { "solidarity": -15, "productivity": 10, "legitimacy": 5, "innovation": 10 }
  },
  "choiceB": {
    "text": "Require office presence",
    "effects": { "solidarity": 10, "productivity": -5, "legitimacy": -5, "innovation": -5 }
  }
}
```
*Why it works*: Explores how modern technology affects social bonds in specialized workplaces.

## Testing Your Cards

1. Add the card to the appropriate array in `cards.json`
2. Refresh the game in your browser
3. Check browser console for JSON parsing errors
4. Play through to see if the card appears and effects feel right
5. Verify the effects make thematic sense

## Connecting to Durkheim

When writing cards, consider these Durkheim concepts:

| Concept | How to incorporate |
|---------|-------------------|
| **Collective conscience** | Shared beliefs, moral outrage, conformity pressure |
| **Division of labor** | Specialization, interdependence, occupational identity |
| **Anomie** | Normlessness during rapid change, unclear rules |
| **Repressive vs. restitutive law** | Punishment for moral violation vs. restoring equilibrium |
| **Occupational groups** | Professional associations, unions, guilds |
| **Social density** | Urbanization, communication, contact between people |

Cards don't need to mention Durkheim explicitly - the game mechanics teach the concepts through experience.

## Quick Checklist

- [ ] Character name is 2-4 words
- [ ] Scenario text is 2-3 sentences
- [ ] Both choices have trade-offs
- [ ] Effects are in reasonable ranges (±5 to ±30)
- [ ] Card fits its era category
- [ ] No obvious "right answer"
- [ ] JSON syntax is valid (watch your commas!)
