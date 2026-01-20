import random
import pygame
import math
import time
# pygame setup
pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock() #what does this do?
running = True

#PLAYER1st
playerImg = pygame.image.load('square48.png')
playerImg2 = pygame.image.load('square32.png')
playerX = 360 #x coords of player
playerY = 480 #y coords of player
playerX_change = 1
playerY_change = 1
def player(x,y):
    screen.blit(playerImg,(x,y))
    screen.blit(playerImg2,(x+10,y+30))
    
def isCollision(dotX, dotY, playerX, playerY):
    distance = math.sqrt(math.pow(dotX - playerX, 2) + (math.pow(dotY - playerY, 2)))
    if distance < 27:
        return True
    else:
        return False

#SCORE
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
testX = 10
testY = 10
def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (0, 200, 0))
    screen.blit(score, (x, y))

#DOTS
no_dots = 4
dotImgs = []
dotX = []
dotY =[]#list of coords of all dots
for i in range(no_dots): #to create dots at the start
        dotImgs.append(pygame.image.load('dot.png'))
        dotX.append(random.randint(0,768)) #randomizing coords of dot
        dotY.append(random.randint(0,568))
        
def dots():
    global a
    a=0
    import random
    for i in range(no_dots):
        collision = isCollision(dotX[i],dotY[i], playerX, playerY)
        if collision: #to update dots with each collision
            dotX[i] = random.randint(0,768) #randomizing coords of dot
            dotY[i] = random.randint(0,568)
            a=a+1
        screen.blit(dotImgs[i],(dotX[i],dotY[i]))

#Title
pygame.display.set_caption('1st Game')

#Events
while running:
    # fill the screen with a color to wipe away
    #          RED GREEN BLUE
    screen.fill((0,0,0))
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #MOVEMENT WITH KEYS
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change= -1
            if event.key == pygame.K_RIGHT:
                playerX_change= 1
            if event.key == pygame.K_UP:
                playerY_change= -1
            if event.key == pygame.K_DOWN:
                playerY_change= 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    #Border restrictions or adding to coords
    playerX+= playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 768:
        playerX = 768
    playerY+= playerY_change
    if playerY <= 0:
        playerY = 0
    elif playerY >= 568:
        playerY = 568
        
    player(playerX,playerY)
    dots()
    score_value=score_value +a
    show_score(testX, testY)
    pygame.display.update()
    clock.tick(60)  #Fix flickering, add snake(by combining multiple images)
    
pygame.quit()
print("Game over")
print("Your score is:",score_value)
