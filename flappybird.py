import pygame as pg
import random
import time

# Initialize Pygame
pg.init()

# Load images
background = pg.image.load("images/background.png")
base = pg.image.load("images/base.png")
tube_up = pg.image.load("images/tube.png")
tube_down = pg.transform.flip(tube_up, False, True)
gameoverUI = pg.image.load("images/gameover.png")

bird_frames = [
    pg.image.load("images/bird1.png"),
    pg.image.load("images/bird2.png"),
]

# Animation variables
isAnim = False
anim_index = 0
anim_timer = 0
anim_delay = 200  # ms between each frame
anim_frames = len(bird_frames)

# Global constants
display_x = 288
display_y = 512
SPEED_ADVANCE = 3
FONT = pg.font.SysFont("Comic Sans MS", 50, bold=True)
SCREEN = pg.display.set_mode((display_x, display_y))
pg.display.set_caption("Flappy Bird by Gullotti Diego")
TOLLERANCE = 5
DISTANCE_BETWEEN_TUBES = 50

bird_width = bird_frames[0].get_width()
bird_height = bird_frames[0].get_height()

class tubes:
    def __init__(self):
        self.x = 300
        self.y = random.randint(-75, 150)

    def advanceAndDraw(self):
        self.x -= SPEED_ADVANCE
        SCREEN.blit(tube_up, (self.x, self.y + 210))
        SCREEN.blit(tube_down, (self.x, self.y - 210))

    def tubeCollision(self, birdX, birdY):
        bird_side_dx = birdX + bird_width - TOLLERANCE
        bird_side_sx = birdX + TOLLERANCE
        tube_side_dx = self.x + tube_up.get_width()
        tube_side_sx = self.x

        bird_side_up = birdY + TOLLERANCE
        bird_side_down = birdY + bird_height - TOLLERANCE

        tubi_lato_su = self.y + 110
        tubi_lato_giu = self.y + 210

        if bird_side_dx > tube_side_sx and bird_side_sx < tube_side_dx:
            if bird_side_up < tubi_lato_su or bird_side_down > tubi_lato_giu:
                gameover()

    def spaceBetweenTube(self, birdx):
        tolleranza = 5
        bird_side_dx = birdx + bird_width - tolleranza
        bird_side_sx = birdx + tolleranza
        tubi_side_dx = self.x + tube_up.get_width()
        tubi_side_sx = self.x

        if bird_side_dx > tubi_side_sx and bird_side_sx < tubi_side_dx:
            return True

# Function to handle game over
def gameover():
    SCREEN.blit(gameoverUI, (50, 180))  # Display game over screen
    update()
    rematch = False
    while not rematch:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN and event.key == pg.K_UP:
                initGame()  # Restart the game if UP key is pressed
                rematch = True
            if event.type == pg.QUIT:
                pg.quit()  # Quit the game if window is closed

# Function to initialize the game
def initGame():
    global bird_x, bird_y, bird_vel_y
    global bird_width, bird_height
    global base_x
    global tubi
    global punti
    global is_between_tubes
    global isAnim, anim_index, anim_timer
    bird_x, bird_y = 60, 150  # Initial position of the bird
    bird_width, bird_height = bird_width, bird_height
    bird_vel_y = 0  # Initial velocity of the bird
    base_x = 0  # Initial position of the base
    tubi = []  # List of tubes
    tubi.append(tubes())  # Add the first tube
    punti = 0  # Initial score
    is_between_tubes = False  # Flag to check if bird is between tubes
    isAnim = False  # Animation flag
    anim_index = 0  # Animation index
    anim_timer = 0  # Animation timer

# Function to draw objects on the screen
def drawObjects():
    SCREEN.blit(background, (0, 0))  # Draw background
    for t in tubi:
        t.advanceAndDraw()  # Draw tubes
    if isAnim:
        rotated_bird = pg.transform.rotate(bird_frames[anim_index], -bird_vel_y * 3)  # Rotate bird based on velocity
        bird_rect = rotated_bird.get_rect(center=(bird_x + bird_width // 2, bird_y + bird_height // 2))
        SCREEN.blit(rotated_bird, bird_rect.topleft)  # Draw rotated bird
    else:
        rotated_bird = pg.transform.rotate(bird_frames[0], -bird_vel_y * 3)
        bird_rect = rotated_bird.get_rect(center=(bird_x + bird_width // 2, bird_y + bird_height // 2))
        SCREEN.blit(rotated_bird, bird_rect.topleft)
    SCREEN.blit(base, (base_x, 400))  # Draw base
    punti_render = FONT.render(str(punti), True, (164, 238, 150))  # Render score
    SCREEN.blit(punti_render, (display_x - 150, 0))  # Draw score

# Function to update the display
def update():
    global clock
    clock = pg.time.Clock()
    FPS = 60
    pg.display.update()
    clock.tick(FPS)

# Initialize variables
initGame()
time.sleep(2)

while True:
    # Base movement illusion
    base_x -= SPEED_ADVANCE
    if base_x < -45:
        base_x = 0

    # Gravity effect
    bird_vel_y += 0.5
    bird_y += bird_vel_y

    for event in pg.event.get():
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            bird_vel_y = 0
            bird_vel_y -= 6
            isAnim = True
            anim_timer = 0
            anim_index = 0
        if event.type == pg.QUIT:
            pg.quit()

    # Animation logic
    if isAnim:
        anim_timer += clock.get_time()
        if anim_timer > anim_delay:
            anim_timer = 0
            anim_index += 1
            if anim_index >= anim_frames:
                isAnim = False
                anim_index = 0

    # Spawn new tubes
    if tubi[-1].x < DISTANCE_BETWEEN_TUBES:
        tubi.append(tubes())

    # Check for collisions with tubes
    for t in tubi:
        t.tubeCollision(bird_x, bird_y)

    # Check for collision with the base
    if bird_y >= 385:
        gameover()

    # Update display
    drawObjects()
    update()

    # Count points
    if not is_between_tubes:
        for t in tubi:
            if t.spaceBetweenTube(bird_x):
                is_between_tubes = True
                break
    if is_between_tubes:
        is_between_tubes = False
        for t in tubi:
            if t.spaceBetweenTube(bird_x):
                is_between_tubes = True
                break
        if not is_between_tubes:
            punti += 1