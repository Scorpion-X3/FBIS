# FBIS
Fencing Bout Information System – a Python tool to log and analyze fencing bout data, designed to identify trends in scoring patterns.

## Features
- Validates bout type (DE vs Pool) and score format
- Ensures scoring rules are enforced (no ties, correct max score)
- Tracks individual touches (attack, parry, remise, counter)
- Associates each touch with the scorer (me vs opponent)
- Identifies most frequent scoring actions using frequency analysis
- Stores bout data persistently using JSON

## Example
Input:
DE or Pool: de  
Score: 15-10  
Touches: attack, parry, attack, counter, ...

Output:
Most Common Touch: attack

## How to Run
1. Clone the repository
2. Run:
   python main.py
3. Follow the prompts in the terminal

## Project Structure
- main.py → main program logic
- bouts.json → stored bout data

## Future Improvements
- Cross-bout analysis (aggregate statistics across multiple bouts)
- Visualization of touch trends
- GUI or web interface
- Player performance tracking over time

## Motivation
As a fencer, I wanted a way to analyze my bouts beyond just the final score.  
This project was built to track how touches are scored and identify patterns that could improve performance.
