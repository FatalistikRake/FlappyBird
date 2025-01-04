
Flappy Bird is a game developed in Python using Pygame. The goal is to guide a bird through a series of pipes, avoiding collisions and scoring points.

---

## 🛠️ Requirements

Make sure you have the following installed on your system:

- Python 3.8 or higher
- [Pygame](https://www.pygame.org/) 2.0 or higher

---

## 💾 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/FatalistikRake/FlappyBird.git
   cd flappy-bird
   ```

2. Install the dependencies:
   ```bash
   pip install pygame
   ```

3. Ensure the project has the following file structure:
   ```
   flappy-bird/
   ├── flappybird.py
   ├── images/
   │   ├── background.png
   │   ├── base.png
   │   ├── bird1.png
   │   ├── bird2.png
   │   ├── tube.png
   │   ├── gameover.png
   ```

---

## 🎮 How to Play

1. Run the game:
   ```bash
   python flappybird.py
   ```

2. Press the spacebar to make the bird fly.
3. Avoid colliding with the pipes and the ground to keep playing.
4. After **Game Over**, press the **up arrow key** to restart the game.

---

## ⚙️ Technical Details

### 1. **Movement and Animation**
- The bird's animation is handled using an array of images (`bird_frames`) and a timer system (`anim_timer`).
- The bird's rotation is dynamically calculated based on its vertical velocity (`bird_vel_y`).

### 2. **Pipes**
- Pipes are instances of the `tubes` class. 
- Each pipe is drawn using two images: one oriented normally (`tube_up`) and the other flipped (`tube_down`).
- The `tubeCollision()` function checks for collisions between the bird and the pipes by calculating the boundaries of each object.

### 3. **Game Over Handling**
- The `gameover()` function displays the Game Over interface and allows the player to restart the game or exit.

---

## 🗂️ Code Structure

### Main Functions

- **`initGame()`**: Initializes all global variables to start a new game.
- **`drawObjects()`**: Draws game elements (background, bird, pipes, base, score).
- **`update()`**: Updates the screen and maintains a framerate of 60 FPS.
- **`gameover()`**: Manages the Game Over interface and logic.

### Class `tubes`
- **`advanceAndDraw()`**: Moves the pipes to the left and draws them on the screen.
- **`tubeCollision()`**: Checks for collisions between the bird and the pipes.
- **`spaceBetweenTube()`**: Determines if the bird has passed between the pipes to increment the score.
