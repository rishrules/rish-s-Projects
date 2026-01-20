import random
import pygame
import math

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

# PLAYER
playerImg = pygame.image.load('square48.png')
playerImg2 = pygame.image.load('square32.png')
playerX = 360  # initial x coordinate of player
playerY = 480  # initial y coordinate of player
playerX2 = 340        # initial x coordinate of square2
playerY2 = 550        # initial y coordinate of square2
PLAYER_SPEED = 5  # speed of player movement per frame

def player(x, y, w, z):
    screen.blit(playerImg, (x, y))
    screen.blit(playerImg2, (w, z))

def isCollision(dotX, dotY, playerX, playerY):
    distance = math.sqrt(math.pow(dotX - playerX, 2) + math.pow(dotY - playerY, 2))
    if distance < 27:
        return True
    else:
        return False

# SCORE
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
testX = 10
testY = 10

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (0, 200, 0))
    screen.blit(score, (x, y))

# DOTS
no_dots = 4
dotImgs = []
dotX = []
dotY = []  # list of coords of all dots
for i in range(no_dots):  # create dots at the start
    dotImgs.append(pygame.image.load('dot.png'))
    dotX.append(random.randint(0, 768))  # randomizing coords of dot
    dotY.append(random.randint(0, 568))

def dots():
    global a
    a = 0
    for i in range(no_dots):
        collision = isCollision(dotX[i], dotY[i], playerX, playerY)
        if collision:  # update dots with each collision
            dotX[i] = random.randint(0, 768)  # randomizing coords of dot
            dotY[i] = random.randint(0, 568)
            a += 1
        screen.blit(dotImgs[i], (dotX[i], dotY[i]))

def direction(playerX, playerY, mouseX, mouseY, playerX2, playerY2):
    # Getting the mouse position
    mouseX, mouseY = pygame.mouse.get_pos()

    # Calculate distance and direction from player to mouse
    dx = mouseX - playerX
    dy = mouseY - playerY
    distance = math.sqrt(dx * dx + dy * dy)
    dx2 = playerX - playerX2
    dy2 = playerY - playerY2
    distance2 = math.sqrt(dx2 * dx2 + dy2 * dy2)
    if distance > 1:
        dx_norm = dx / distance
        dy_norm = dy / distance
        dx2_norm = dx2 / distance2
        dy2_norm = dy2 / distance2
       

        # Move the player towards the cursor
        playerX += dx_norm * PLAYER_SPEED
        playerY += dy_norm * PLAYER_SPEED
        playerX2 += dx2_norm * PLAYER_SPEED
        playerY2 += dy2_norm * PLAYER_SPEED


# Title
pygame.display.set_caption('1st Game - Mouse Movement')

# Events
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    mouseX, mouseY = pygame.mouse.get_pos()
    direction(playerX, playerY, mouseX, mouseY, playerX2, playerY2)

    # Boundary restrictions
    if playerX <= 0:
        playerX = 0
    elif playerX >= 768:
        playerX = 768
    if playerY <= 0:
        playerY = 0
    elif playerY >= 568:
        playerY = 568

    player(playerX, playerY, playerX2, playerY2)
    dots()
    score_value += a  
    show_score(testX, testY)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
print("Game over")
print("Your score is:", score_value)

