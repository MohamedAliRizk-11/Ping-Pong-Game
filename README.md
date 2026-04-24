# 🏓 Ping Pong AI Game (Python + Pygame)

![Game Logo](resources/logo.png)

A **Ping Pong game** built using **Python (Pygame)** with an intelligent AI opponent and special power-ups like **Fire, Ice, and Scissors** that change gameplay dynamically and make the match more exciting.

The game is not just classic ping pong — it includes **special effects, AI movement using BFS algorithm, and interactive gameplay mechanics.**

---

# 🎮 Game Features

### ✨ Core Gameplay:
1. Player vs AI Ping Pong match.
2. Smooth paddle movement using mouse control.
3. Real-time scoring system.
4. Ball physics with randomized bounce effect.

---

### 🔥 Power-ups System:

1. **Fire 🔥**
   - Increases ball speed instantly.
   - Makes gameplay harder for both players.

2. **Ice ❄️**
   - Freezes opponent temporarily.
   - Prevents paddle movement for a short time.

3. **Scissors ✂️**
   - Shrinks opponent paddle size.
   - Makes defending harder.

---

### 🤖 AI System:
- AI uses **BFS Algorithm** to predict ball movement.
- Smart tracking instead of random movement.
- Difficulty increases naturally during gameplay.

---

# 🧠 Game Logic Highlights

- Collision detection between ball and paddles.
- Dynamic speed boosting system.
- Temporary status effects (Freeze / Cut).
- Random item spawning system.
- Score reset system after goal.

---

# 🖥️ Game Flow

START SCREEN  
↓  
PRESS START  
↓  
GAME PLAY (Player vs AI)  
↓  
SCORE UPDATE  
↓  
CONTINUE MATCH  

---

# 🎮 Screenshots

### 🏁 Start Screen
![Start Screen](resources/start.png)

### 🏓 Gameplay
<p float="left">
  <img src="resources/game1.png" width="400"/>
  <img src="resources/game2.png" width="400"/>
</p>

### ⚡ Power-ups in action
<p float="left">
  <img src="resources/fire.png" width="200"/>
  <img src="resources/ice.png" width="200"/>
  <img src="resources/scissors.png" width="200"/>
</p>

---

# ⚙️ Requirements

- Python 3.x
- Pygame

Install dependencies:
```bash
pip install pygame
