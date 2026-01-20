import random
import pygame
import math

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()  # This controls the frame rate of the game
running = True

class Player:
    def __init__(self, image, start_x, start_y, controls):
        self.image = image
        self.x = start_x
        self.y = start_y
        self.x_change = 0
        self.y_change = 0
        self.controls = controls  # Dictionary for control keys

    def handle_keydown(self, key):
        if key == self.controls['left']:
            self.x_change = -1
        elif key == self.controls['right']:
            self.x_change = 1
        if key == self.controls['up']:
            self.y_change = -1
        elif key == self.controls['down']:
            self.y_change = 1

    def handle_keyup(self, key):
        if key == self.controls['left'] or key == self.controls['right']:
            self.x_change = 0
        if key == self.controls['up'] or key == self.controls['down']:
            self.y_change = 0

    def update_position(self):
        self.x += self.x_change
        self.y += self.y_change

        # Keep in screen bounds
        if self.x < 0:
            self.x = 0
        elif self.x > 768:
            self.x = 768
        if self.y < 0:
            self.y = 0
        elif self.y > 568:
            self.y = 568

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

def isCollision(dotX, dotY, playerX, playerY):
    distance = math.sqrt(math.pow(dotX - playerX, 2) + (math.pow(dotY - playerY, 2)))
    return distance < 27

# Load images
playerImg1 = pygame.image.load('square48.png')
playerImg2 = pygame.image.load('square32.png')

# Controls for players
player1_controls = {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT, 'up': pygame.K_UP, 'down': pygame.K_DOWN}
player2_controls = {'left': pygame.K_a, 'right': pygame.K_d, 'up': pygame.K_w, 'down': pygame.K_s}

# Create Player instances
player1 = Player(playerImg1, 360, 480, player1_controls)
player2 = Player(playerImg2, 400, 480, player2_controls)

# SCORE
score_value1 = 0
score_value2 = 0
font = pygame.font.Font('freesansbold.ttf', 32)
testX = 10
testY = 10

def show_score(x, y, score):
    score_display = font.render("Score : " + str(score), True, (0, 200, 0))
    screen.blit(score_display, (x, y))

# DOTS
no_dots = 8
dotImgs = []
dotX = []
dotY = []  # list of coords of all dots
for i in range(no_dots):  # to create dots at the start
    dotImgs.append(pygame.image.load('dot.png'))
    dotX.append(random.randint(0, 768))  # randomizing coords of dot
    dotY.append(random.randint(0, 568))

def dots():
    global a1, a2
    a1 = 0
    a2 = 0
    for i in range(no_dots):
        collision1 = isCollision(dotX[i], dotY[i], player1.x, player1.y)
        collision2 = isCollision(dotX[i], dotY[i], player2.x, player2.y)
        if collision1:  # Player 1 collision
            dotX[i] = random.randint(0, 768)  # randomizing coords of dot
            dotY[i] = random.randint(0, 568)
            a1 += 1
        if collision2:  # Player 2 collision
            dotX[i] = random.randint(0, 768)  # randomizing coords of dot
            dotY[i] = random.randint(0, 568)
            a2 += 1
        screen.blit(dotImgs[i], (dotX[i], dotY[i]))

# Title
pygame.display.set_caption('Multiplayer Game')

# Events
while running:
    screen.fill((0, 0, 0))  # fill the screen with a color to wipe away
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Handle input for Player 1
        if event.type == pygame.KEYDOWN:
            player1.handle_keydown(event.key)
        if event.type == pygame.KEYUP:
            player1.handle_keyup(event.key)

        # Handle input for Player 2
        if event.type == pygame.KEYDOWN:
            player2.handle_keydown(event.key)
        if event.type == pygame.KEYUP:
            player2.handle_keyup(event.key)

    # Update positions
    player1.update_position()
    player2.update_position()

    # Draw players and dots
    player1.draw()
    player2.draw()
    dots()

    # Update scores
    score_value1 += a1
    score_value2 += a2
    show_score(testX, testY, score_value1)  # Show score for Player 1
    show_score(testX, testY + 40, score_value2)  # Show score for Player 2

    pygame.display.update()
    clock.tick(60)  # Fix flickering, add snake (by combining multiple images)

pygame.quit()
print("Game over")
print("Your score is Player 1:", score_value1)
print("Your score is Player 2:", score_value2)
