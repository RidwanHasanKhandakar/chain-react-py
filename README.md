# Chain Reaction Game (Python + Pygame)

A multiplayer recreation of the classic **Chain Reaction** strategy game built using **Python** and **Pygame**.

This project focuses on:
- Grid-based game mechanics
- Chain reaction overflow system
- Turn-based multiplayer gameplay
- Recursive explosion logic
- Dynamic player support

---

## 🎮 Gameplay

Players take turns placing orbs on a grid.

Each cell has a critical mass depending on its position:

- Corner cells → explode at 2 orbs
- Edge cells → explode at 3 orbs
- Middle cells → explode at 4 orbs

When a cell reaches critical mass:
- It explodes
- Sends one orb to neighboring cells
- Converts neighboring cells to the current player's color
- Can trigger massive chain reactions

The last remaining player wins.

---

## ✨ Features

- 2–4 player support
- Dynamic player name input
- Turn-based gameplay
- Real-time chain reactions
- Recursive overflow mechanics
- Orb visualization system
- Win detection system
- Restart and quit functionality

---

## 🛠️ Technologies Used

- Python 3
- Pygame

---

## 📂 Project Structure

```text
project/
│
├── main.py
└── README.md
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

### 2. Install Pygame

```bash
pip install pygame
```

### 3. Run the game

```bash
python main.py
```

---

## 🎯 Controls

| Key / Action | Function |
|---|---|
| Mouse Click | Place orb |
| R | Restart game |
| Q | Quit game |

---

## 🧠 Concepts Used

This project implements several important programming concepts:

- Object-Oriented Programming (OOP)
- 2D Grid Systems
- Recursive Algorithms
- Event Handling
- State Management
- Dynamic Rendering

---

## 🔥 Overflow System

Each cell stores:
- Orb count
- Player ownership
- Neighbor references

When a cell exceeds its critical limit:

1. The cell explodes
2. Neighbor cells receive orbs
3. Ownership spreads
4. More explosions may occur recursively

This creates the game's signature chain reaction effect.

---

## ⚠️ Current Limitations

- Overflow system uses recursion
- No AI opponents yet
- No sound effects
- No animations
- Local multiplayer only
- Single-file architecture

---

## 🚀 Future Improvements

Planned upgrades:
- Queue-based overflow engine
- Better animations
- Sound effects
- AI opponents
- Online multiplayer
- Improved UI/UX
- Modular architecture
- Web version using HTML/CSS/JavaScript


## 👨‍💻 Author

**Rahin**  
Computer Science Student

---

## 📄 License

This project is for educational and personal learning purposes.
