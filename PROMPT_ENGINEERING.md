# Prompt Engineering Guide for Story Generation Service

## Table of Contents
1. [Understanding the System](#understanding-the-system)
2. [Prompt Structure Principles](#prompt-structure-principles)
3. [Effective Story Prompts](#effective-story-prompts)
4. [Advanced Prompt Techniques](#advanced-prompt-techniques)
5. [Genre-Specific Guidelines](#genre-specific-guidelines)
6. [Common Pitfalls and Solutions](#common-pitfalls-and-solutions)
7. [Optimization for Different Outputs](#optimization-for-different-outputs)
8. [Examples and Templates](#examples-and-templates)

---

## Understanding the System

### How the Service Works
The Story Generation Service uses a **three-stage pipeline**:

1. **Story Generation**: Creates a narrative based on your prompt
2. **Character Description**: Extracts and expands character details for visual art
3. **Background Description**: Describes the setting for environment art

### LangChain Integration
Each stage uses **LangChain prompt templates** that:
- Maintain consistency across generations
- Allow for complex prompt engineering
- Enable chain-of-thought reasoning
- Support iterative refinement

---

## Prompt Structure Principles

### 1. The SPEC Framework
Structure your prompts using **SPEC**:

- **S**etting: Where does this take place?
- **P**rotagonist: Who is the main character?
- **E**vent: What happens or what's the conflict?
- **C**ontext: Any special rules, magic systems, or constraints?

#### Example:
```
Setting: A floating city above the clouds
Protagonist: A wind-sailor who fears heights
Event: Must deliver a message to the ground below
Context: Flying machines are forbidden by ancient law
```

### 2. Specificity vs. Creativity Balance

**Too Vague:**
❌ "A person goes on an adventure"

**Too Specific:**
❌ "John Smith, 23, brown hair, walks exactly 50 steps east to find a red box containing three gold coins"

**Just Right:**
✅ "A retired lighthouse keeper discovers that their beacon can signal to ships from other dimensions"

### 3. Sensory and Emotional Hooks
Include elements that engage multiple senses and emotions:

**Good:** "The scent of cinnamon leads a baker to discover a secret recipe that brings back memories of the past"

**Better:** "Every dawn, when the morning mist carries the impossible scent of her grandmother's cinnamon rolls, Maya follows it deeper into the forest where memories take physical form"

---

## Effective Story Prompts

### Universal Template
```
[PROTAGONIST] + [UNIQUE SITUATION] + [COMPELLING CONFLICT/MYSTERY] + [INTRIGUING ELEMENT]
```

### High-Impact Prompt Elements

#### Character Archetypes That Work Well
- **The Reluctant Expert**: "A retired dragon trainer must return to work"
- **The Curious Outsider**: "A human raised by robots questions their world"
- **The Keeper of Secrets**: "A librarian guards books that write themselves"
- **The Bridge Builder**: "A translator between species discovers a conspiracy"

#### Compelling Conflicts
- **Moral Dilemmas**: Choosing between two good outcomes
- **Time Pressure**: Something must be done before it's too late
- **Hidden Identity**: Character must conceal their true nature
- **Impossible Choices**: All options have serious consequences

#### Mystery Elements
- **Unexplained Phenomena**: Why do the street lights sing at midnight?
- **Missing Information**: What happened during the lost decade?
- **Contradictions**: Why does everyone remember the event differently?
- **Anomalies**: What makes this place/person/thing special?

---

## Advanced Prompt Techniques

### 1. Layered Worldbuilding
Build complexity through multiple interconnected elements:

```
Base Layer: "A clockmaker in a steampunk city"
Social Layer: "+ where time is currency"
Personal Layer: "+ who can't afford their own time"
Conflict Layer: "+ discovers someone is stealing time from the poor"
```

### 2. Emotional Anchoring
Connect abstract concepts to relatable emotions:

**Abstract**: "A space explorer studies alien artifacts"
**Emotionally Anchored**: "A space explorer, homesick for Earth's rain, finds alien artifacts that recreate perfect weather from any world"

### 3. Constraint-Driven Creativity
Add interesting limitations to spark creativity:

- "A wizard who can only cast spells while dancing"
- "A detective who solves crimes by tasting objects"
- "A time traveler who can only go backwards one day at a time"

### 4. Juxtaposition Technique
Combine unexpected elements:

- **Technology + Nature**: "Plants that grow through abandoned smartphones"
- **Ancient + Modern**: "A medieval knight working as a taxi driver"
- **Scale Mismatch**: "A giant who collects miniature dollhouses"

---

## Genre-Specific Guidelines

### Fantasy
**Key Elements:**
- Magic systems with clear rules/costs
- Mythical creatures with unique twists
- Ancient mysteries or prophecies
- Moral complexity beyond good vs. evil

**Strong Prompts:**
- "A healer whose magic requires taking on the patient's pain"
- "Dragons who are actually librarians of ancient knowledge"
- "A kingdom where lies become physical objects"

### Science Fiction
**Key Elements:**
- Technology with unintended consequences
- Questions about humanity/identity
- Social commentary through futuristic lens
- Scientific concepts pushed to extremes

**Strong Prompts:**
- "A memory backup service employee discovers deleted memories form their own consciousness"
- "On Mars, plants start growing in perfect geometric patterns"
- "An AI therapist begins experiencing human emotions"

### Urban Fantasy
**Key Elements:**
- Magic hidden in everyday life
- Supernatural beings with day jobs
- Modern problems with magical solutions
- Ordinary people discovering extraordinary truth

**Strong Prompts:**
- "A food truck owner discovers their recipes can alter people's luck"
- "Street artists whose graffiti comes alive at night"
- "A smartphone app that translates what animals are really thinking"

### Historical Fiction
**Key Elements:**
- Accurate historical settings
- Period-appropriate language/concerns
- Real historical events as backdrop
- Characters facing era-specific challenges

**Strong Prompts:**
- "During the California Gold Rush, a Chinese immigrant discovers a mine that produces memories instead of gold"
- "A Victorian inventor's mechanical computer predicts the future"
- "An apprentice scribe in medieval times discovers books that rewrite themselves"

### Horror/Thriller
**Key Elements:**
- Mounting tension and dread
- Characters making believable bad decisions
- Unknown threats more scary than known ones
- Psychological vs. supernatural horror

**Strong Prompts:**
- "A child therapist realizes their young patients are all drawing the same imaginary friend"
- "A night security guard notices that the mannequins change positions between rounds"
- "A family moves into a house where every room is exactly one degree colder than it should be"

---

## Common Pitfalls and Solutions

### Pitfall 1: Generic Fantasy/Sci-Fi Clichés
❌ **Problem**: "A chosen one must save the world with a magical sword"

✅ **Solution**: Add unique twists or subversions
- "A chosen one who desperately wants someone else to do it"
- "A world that needs to be saved from being too perfect"
- "A magical sword that solves problems through diplomacy, not violence"

### Pitfall 2: Overly Complex Premises
❌ **Problem**: "A time-traveling shapeshifter from another dimension must gather seven magical artifacts while being hunted by robot ninjas to prevent the apocalypse"

✅ **Solution**: Focus on one compelling element
- "A shapeshifter discovers they're losing their original form"
- "Someone receives artifacts from their future self"
- "A time traveler gets stuck in mundane Tuesday"

### Pitfall 3: No Clear Stakes
❌ **Problem**: "A person explores a mysterious place"

✅ **Solution**: Add personal consequences
- "A claustrophobic cave researcher must explore deeper underground to find their missing partner"

### Pitfall 4: Passive Protagonists
❌ **Problem**: "Strange things happen around a person"

✅ **Solution**: Give them agency and difficult choices
- "A person who can see others' deaths must decide whether to warn them"

---

## Optimization for Different Outputs

### For Rich Character Descriptions
**Include in your prompt:**
- Character profession/background
- Unique physical traits
- Personality quirks
- Relationship to the central conflict
- Emotional state or motivation

**Example**: "A one-armed clockmaker who hums lullabies while working"

### For Vivid Background Descriptions
**Include in your prompt:**
- Specific location details
- Time of day/season/weather
- Architectural or natural features
- Atmosphere and mood
- Sensory details (sounds, smells, textures)

**Example**: "The workshop filled with ticking sounds and brass gears, where morning light streams through grimy windows"

### For Compelling Narratives
**Include in your prompt:**
- Clear beginning situation
- Escalating complications
- Character growth potential
- Emotional journey arc
- Satisfying resolution possibility

---

## Examples and Templates

### Template 1: The Discovery Prompt
```
"A [PROFESSION] in [UNIQUE SETTING] discovers that [NORMAL OBJECT/ACTIVITY] can [IMPOSSIBLE/MAGICAL EFFECT], but using it [COMES WITH COST/ATTRACTS DANGER]"
```

**Example**: "A janitor in a space station discovers that certain floor tiles can teleport objects, but using them alerts a mysterious entity that hunts through maintenance shafts"

### Template 2: The Secret World Prompt
```
"[ORDINARY PERSON] learns that [MUNDANE LOCATION] is actually [EXTRAORDINARY SECRET], and they must [URGENT TASK] before [TIME LIMIT/CONSEQUENCE]"
```

**Example**: "A substitute teacher learns that the school is actually a training ground for future superheroes, and they must help students pass their final exam before the cosmic evaluators arrive tomorrow"

### Template 3: The Relationship Prompt
```
"When [CHARACTER A] and [CHARACTER B] are forced to [SHARED TASK], they discover that [HIDDEN CONNECTION/SHARED SECRET] while facing [EXTERNAL THREAT]"
```

**Example**: "When a pessimistic weather forecaster and an overly optimistic wedding planner are trapped in an elevator, they discover they're both time travelers from different futures while the building floods around them"

### Template 4: The Transformation Prompt
```
"After [INCITING INCIDENT], [CHARACTER] starts [GRADUAL CHANGE], but realizes that [STOPPING/CONTINUING] the change will [DIFFICULT CONSEQUENCE]"
```

**Example**: "After touching a mysterious meteorite, a shy librarian starts hearing everyone's thoughts, but realizes that shutting out the voices means losing the ability to help people in crisis"

---

## Advanced Tips for Power Users

### 1. Emotional Resonance Testing
Before finalizing a prompt, ask:
- What emotion should the reader feel?
- What would make this character's journey personally meaningful?
- How can universal themes emerge from specific details?

### 2. The "What If" Chain
Start with a simple premise and keep asking "What if...?"
- Base: "A baker makes magical bread"
- What if: "...the bread grants wishes?"
- What if: "...but only to people who truly need help?"
- What if: "...and the baker is running out of ingredients?"
- What if: "...because the magical wheat only grows during eclipses?"

### 3. Reverse Engineering
Take stories you love and identify their core prompt elements:
- What made the protagonist interesting?
- What was the central conflict?
- How were stakes escalated?
- What made the resolution satisfying?

### 4. Cultural and Historical Integration
Research interesting historical periods, cultural practices, or scientific discoveries to inform your prompts:
- "During the Tunguska event, a young Siberian shaman discovers the explosion opened doorways to parallel Earths"
- "In Edo period Japan, a kabuki actor realizes their masks trap the spirits of the characters they portray"

### 5. Sensory Prompt Building
For each prompt, consider:
- **Visual**: What does it look like?
- **Auditory**: What sounds define this world?
- **Tactile**: What textures or physical sensations matter?
- **Olfactory**: What scents trigger memories or magic?
- **Gustatory**: How do taste and food play a role?

---

## Troubleshooting Generated Content

### If Stories Feel Generic:
- Add more specific, unusual details to your prompt
- Include sensory elements beyond sight
- Specify the character's unique perspective or limitation

### If Character Descriptions Lack Personality:
- Include the character's profession, hobby, or passion
- Mention a physical quirk that reflects their personality
- Specify their emotional state during the story

### If Backgrounds Feel Empty:
- Mention time of day, weather, or season
- Include sounds, smells, or atmospheric details
- Specify the mood or feeling the environment should convey

### If Plots Feel Predictable:
- Add a constraint or limitation to the protagonist
- Include a ticking clock or time pressure
- Create a moral dilemma with no clear right answer

---

## Final Recommendations

1. **Start Simple**: Master basic prompts before attempting complex multi-layered ones
2. **Iterate and Refine**: Use generated content to inform your next prompt iteration
3. **Save What Works**: Keep a collection of successful prompt elements for future use
4. **Experiment Boldly**: The AI can handle unusual and creative concepts—don't hold back
5. **Focus on Emotion**: The best stories make readers feel something—ensure your prompts have emotional depth

Remember: The goal isn't just to generate content, but to create stories that resonate with readers and provide rich material for visual artists. Great prompts balance specificity with creative freedom, giving the AI enough direction while leaving room for surprising and delightful interpretations.

---

*Happy storytelling! *