# WorldCupCompetitionSystem ⚽

A project from my **first semester** of university.

I remember doing this assignment with a friend and a bunch of curious, confused peers. To this point, most of my coding knowledge at the time was YouTube and tutorials.

## Project Background & Requirements

### 🏗️ Project Requirements

The goal was to create a **World Cup competition system** to simulate the full tournament from the group stage to the final. The key constraints and requirements were:

1. **Use strictly OOP** — *functional programming was officially banned like handballs in the box.*
2. **Create 6 classes**:
   - `TeamClass` → stores info like country, results, players, etc.
   - `GroupStageClass` → represents the 8 groups (A–H) and handles matches/rankings.
   - `Round16Class` → 16-team knockout stage logic.
   - `QuarterFinalClass` → quarterfinal logic.
   - `SemiFinalClass` → semifinal logic.
   - `FinalRoundClass` → grand finale and crowning the world champ.
3. **Create 32 team objects** and assign them to 8 group objects.
4. **Progression logic** must auto-assign qualified teams from each stage to the next (e.g. winners of the group stage go to Round of 16, etc).
5. The **user only inputs the match results**, nothing more.
6. The system must:
   - Print results of each stage
   - Output the final World Cup winner
7. Include any extra features you find useful — *bonus points for creativity and avoiding spaghetti code.*

---

### ⚽ Test Scenarios

You were required to test the system using:
- Real results from **FIFA World Cup 2022** or **FIFA World Cup 2018**
- And also simulate other random results and teams (*chaotic good mode*)

Official 2018 results were to be found via:
[Google FIFA Results](https://www.google.com/search?q=FIFA+World+Cup+winners+list+2022)

## About the Project we ended up doing

This system simulates a World Cup-style football (soccer) tournament:
- Group Stage logic
- Knockout rounds (Round of 16, Quarterfinals, Semifinals, Third Place match, and Final)
- Player and team data tracking
- Match outcomes and progression

I wrote the `Round16`, then **shamelessly copy-pasted** it into `QuarterFinals`, `SemiFinals`, `Third_and_Fourth`, and `FinalRound`. Then I just... tweaked them until it worked. It's possibly the most unoptimized thing you'll ever see in your life.

Coming back to this after learning Java, C++, and C# feels like reading diary entries written by your past self in crayon, especially since Python is tab sensitive.

## Features

- 📝 Create and manage teams with real-world data
- 🧮 Automatically calculate group stage results (MP, W, D, L, GF, GA, GD, Pts)
- 🔄 Progress teams through each knockout round
- 📊 Track players by position
- 💾 Save and load team data using JSON

## Project Structure

```
.
├── json_data/
│   ├── 2022_data.json               # Team data and results from the actual 2022 World Cup
│   ├── 2022_blank_data.json         # Empty template to be populated by the program
│   ├── 2022_create_random_data.json# Randomized team data and results (simulated)
│   └── 2022_saving_data.json        # Stores user-input team data and results
│
├── classes/
│   ├── team_class.py                # Defines the TeamClass and its methods
│   ├── group_stage_class.py         # Group stage match logic and ranking
│   ├── round_16_class.py            # Round of 16 knockout stage
│   ├── quarter_final_class.py       # Quarterfinals knockout stage
│   ├── semi_final_class.py          # Semifinals knockout stage
│   ├── third_n_fourth_class.py      # Match to determine 3rd place
│   └── final_round_class.py         # Final match to determine the champion
│
├── jupyter_notebooks_files/
│   ├── team_class.ipynb             # Notebook version of team class
│   ├── group_stage_class.ipynb      # Notebook version of group stage logic
│   ├── round_16_round_class.ipynb   # Notebook version of Round of 16 logic
│   ├── q_final_round_class.ipynb    # Notebook version of quarterfinals
│   ├── s_final_round_class.ipynb    # Notebook version of semifinals
│   ├── third_and_fourth_round_class.ipynb # Notebook version of 3rd place match
│   └── final_round_class.ipynb      # Notebook version of the final match
│
├── world_cup_competition_system_(13).ipynb # Main entry point (yes, the name is cursed)
└── README.md
```

## Technologies

- Python
- JSON (for data persistence)
- Terminal I/O only (no GUI)

## To Run the Project

```bash
python world_cup_competition_system_(13).ipynb
```

Make sure your all .json files exists in a `json_data/` directory. You can either populate it manually or through the interface.

## Reflections

Looking back, this was:
- 🧠 My first real Python project
- 🤝 A true team effort
- 💡 An unintentionally great crash course in how *not* to structure code

Now that I understand classes, design patterns, and efficiency, this is a perfect candidate for a future refactor — or maybe just a museum piece of my past mistakes.

---

> “You don’t need to see my code. Just know that it works… mostly.”  
– Me, aged 19 and clueless.
