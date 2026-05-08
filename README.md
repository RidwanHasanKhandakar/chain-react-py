Chain Reaction Game (Python + Pygame)

A multiplayer recreation of the classic mobile strategy game Chain Reaction, built using Python and Pygame.

This project focuses on:

Grid-based game logic
Chain reaction mechanics
Turn-based gameplay
Recursive overflow system
Dynamic multiplayer support
🎮 Gameplay Overview

Players take turns placing orbs on a grid.

Each cell has a critical mass based on its position:

Corner cells → explode at 2
Edge cells → explode at 3
Middle cells → explode at 4

When a cell reaches critical mass:

It explodes
Sends one orb to each neighboring cell
Converts neighboring cells to the current player's color
Can trigger massive chain reactions

The last remaining player wins.

✨ Features
✅ 2–4 player support
✅ Dynamic player name input
✅ Real-time chain reactions
✅ Recursive overflow mechanics
✅ Turn-based gameplay
✅ Orb visualization system
✅ Win detection system
✅ Restart and quit functionality
🛠️ Technologies Used
Python 3
Pygame
📂 Project Structure
project/
│
├── main.py
└── README.md
🚀 Installation
1. Clone the repository
git clone <your-repository-link>
cd <project-folder>
2. Install Pygame
pip install pygame
3. Run the game
python main.py
🎯 Controls
Key / Action	Function
Mouse Click	Place orb
R	Restart game
Q	Quit game
🧠 Core Concepts Used

This project implements several important programming and game development concepts:

Object-Oriented Programming (OOP)
2D Grid Systems
Recursive Algorithms
Event Handling
Collision-style Chain Reactions
Dynamic Rendering
State Management
🔥 How the Overflow System Works

Each grid cell stores:

Orb count
Player ownership
Neighbor references

When a cell exceeds its critical limit:

The cell resets
Neighbor cells receive orbs
Ownership spreads
Additional explosions may occur recursively

This creates the game's signature chain reaction effect.

⚠️ Current Limitations
Overflow system uses recursion
No AI opponents yet
No animations or sound effects
Local multiplayer only
Single-file architecture
🚀 Future Improvements

Planned upgrades include:

Queue-based overflow engine
Better animations
Sound effects
AI opponents
Online multiplayer
Improved UI/UX
Modular code architecture
Web version using HTML/CSS/JavaScript
📸 Screenshots

Add screenshots here later.
<img width="1457" height="1000" alt="Screenshot 2026-05-07 223959" src="https://github.com/user-attachments/assets/0bec5f02-cbe4-476b-b321-f0b4dc805e63" />


📚 Learning Goals

This project was created to practice:

Game logic design
System architecture
Real-time rendering
Interactive programming with Pygame
👨‍💻 Author

Rahin
Computer Science Student
Built using Python and Pygame

📄 License

This project is for educational and personal learning purposes.
