import pygame
import time
import random

pygame.init()

# R,G,B - SomeColors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (17, 124, 47)
blue = (0, 0, 255)

#LoadingImages
sunImg = pygame.image.load("images/bgSunset1.png")
dogImg = pygame.image.load("images/pixdogimage.png")
clickedDogImg = pygame.image.load("images/clickeddog.png")
dog2Img = pygame.image.load("images/dog2image.png")
clickedDog2Img = pygame.image.load("images/clickeddog2.png")
boneImg = pygame.image.load("images/boneimage.png")
chocolateImg = pygame.image.load("images/chocolateimage.png")
vacuumImg = pygame.image.load("images/vacuum.png")
startImg = pygame.image.load("images/starticon.png")
quitImg = pygame.image.load("images/quiticon.png")
titleImg = pygame.image.load("images/titleicon.png")
clickStartImg = pygame.image.load("images/clickedStartIcon.png")
clickQuitImg = pygame.image.load("images/clickedQuitIcon.png")
selectText = pygame.image.load("images/selectscreentext.png")

#SettingFrame
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Dodgin' Doggo")

#SettingClock
clock = pygame.time.Clock()

#PlayerClassParameters
playerparms = []
dog1parms = [dogImg, 5, 377, 450, 36, 30, 1.1]
dog2parms = [dog2Img,3.5,380,510,30,25, 1.02]
#ButtonClass
class Button:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            gameDisplay.blit(img_act,(x_act, y_act))
            if click[0] and action != None:
                time.sleep(2)
                action()
        else:
            gameDisplay.blit(img_in,(x,y))
#ButtonsForCharacterSelection
class Button2:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, parms, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            gameDisplay.blit(img_act, (x_act, y_act))
            if click[0] and action != None:
                playerparms.append(parms[0])
                playerparms.append(parms[1])
                playerparms.append(parms[2])
                playerparms.append(parms[3])
                playerparms.append(parms[4])
                playerparms.append(parms[5])
                playerparms.append(parms[6])
                time.sleep(2)
                action()
        else:
            gameDisplay.blit(img_in, (x, y))

# BackgroundClass
class Background:
    def __init__(self, bg_img, bg_x, bg_y):
        self.bg_x = bg_x
        self.bg_y = bg_y
        gameDisplay.blit(bg_img, (bg_x, bg_y))

# PlayerClass
class Player:
    def __init__(self,p_img,speedIn,dog_x,dog_y,hitbox_x,hitbox_y,speedmultiplier):
        self.speed = speedIn
        self.dog_x = dog_x
        self.dog_y = dog_y
        self.p_img = p_img
        self.hitbox_x = hitbox_x
        self.hitbox_y = hitbox_y
        self.speedmult = speedmultiplier


# GameObjectsClass
class Gameobject:
    def __init__(self, b_image, speed, coord_x, coord_y, hitbox_x, hitbox_y):
        self.b_image = b_image
        self.speed = speed
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.hitbox_x = hitbox_x
        self.hitbox_y = hitbox_y

# ScoreFunction
def scorecounter(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score:" + str(count), True, black)
    gameDisplay.blit(text, (0, 0))

# CrashFunction/MessageDisplay
def text_objects(text, font):
    textsurface = font.render(text, True, blue)
    return textsurface, textsurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf", 46)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()


def crash(message):
    message_display(message)

#QuitFunction
def quitgame():
    pygame.quit()
    quit()

#MainMenu
def mainmenu():

    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)

        titletext = gameDisplay.blit(titleImg, (275,200))
        startButton = Button(startImg,280,260,60,20,clickStartImg,273,258,selectScreen)
        quitButton = Button(quitImg,475,260,60,20,clickQuitImg,470,258,quitgame)

        pygame.display.update()
        clock.tick(15)

#CharacterSelect
def selectScreen():
    select = True

    while select:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        gameDisplay.blit(selectText,(200,150))
        dogSelect = Button2(dogImg, 280,260,40,150,clickedDogImg,278,226,dog1parms,game_loop)
        dog2select = Button2(dog2Img,480,260,40,100, clickedDog2Img,479,239,dog2parms,game_loop)

        pygame.display.update()
        clock.tick(15)

#MainGame
def game_loop():
#CreatingObjects
    dog = Player(playerparms[0],playerparms[1],playerparms[2],playerparms[3],playerparms[4],playerparms[5],playerparms[6])
    bone = Gameobject(boneImg, 5, random.randrange(0, display_width - 20),-600,40,35)
    chocolate1 = Gameobject(chocolateImg, 3, random.randrange(0, display_width - 20),-600,40,35)
    chocolate2 = Gameobject(chocolateImg, 3, random.randrange(0, display_width - 20),-1000,40,35)
    vacuum = Gameobject(vacuumImg, 4, random.randrange(0, display_width - 20),random.randrange(-2000, -1000),55,100)
#Constants
    x_change = 0
    score = 0

    gameexit = False
#GameLoop
    while not gameexit:

#Background
        gameDisplay.fill(white)
        bg = Background(sunImg, 0, 0)
# Objects
        gameDisplay.blit(bone.b_image, (bone.coord_x, bone.coord_y))
        gameDisplay.blit(chocolate1.b_image, (chocolate1.coord_x, chocolate1.coord_y))
        gameDisplay.blit(chocolate2.b_image, (chocolate2.coord_x, chocolate2.coord_y))
        gameDisplay.blit(vacuum.b_image, (vacuum.coord_x, vacuum.coord_y))
#Player
        gameDisplay.blit(dog.p_img, (dog.dog_x,dog.dog_y))

#Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dog.dog_x > 0:
                    x_change = dog.speed*-1 + -1*dog.speedmult*score
                elif event.key == pygame.K_RIGHT and dog.dog_x < display_width - 45:
                    x_change = dog.speed + dog.speedmult*score
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        dog.dog_x += x_change

        # print(event)

# ObjectSpeeds
        bone.coord_y += bone.speed
        chocolate1.coord_y += chocolate1.speed + 1.2 * score
        chocolate2.coord_y += chocolate1.speed + 1.2 * score
        vacuum.coord_y += vacuum.speed
        # if score >= 1:
        # vac_y += 10

# Boundaries
        if dog.dog_x > display_width - dog.hitbox_x or dog.dog_x < 0:
            x_change = 0

# RecallingObjects
        if bone.coord_y > display_height:
            bone.coord_y = -10
            bone.coord_x = random.randrange(0, display_width - 25)
        if chocolate1.coord_y > display_height - 10:
            chocolate1.coord_y = -10
            chocolate1.coord_x = random.randrange(0, display_width - 25)
        if chocolate2.coord_y > display_height:
            chocolate2.coord_y = -410
            chocolate2.coord_x = random.randrange(0, display_width - 25)
        if vacuum.coord_y > display_height:
            vacuum.coord_y = -2000
            vacuum.coord_x = random.randrange(0, display_width - 56)
# Score
        scorecounter(score)

# Collisons
    # Choc
        if dog.dog_y < chocolate1.coord_y + chocolate1.hitbox_y and dog.dog_y > chocolate1.coord_y or dog.dog_y + dog.hitbox_y > chocolate1.coord_y and dog.dog_y + dog.hitbox_y < chocolate1.coord_y + chocolate1.hitbox_y:
            if dog.dog_x > chocolate1.coord_x and dog.dog_x < chocolate1.coord_x + chocolate1.hitbox_x or dog.dog_x + dog.hitbox_x > chocolate1.coord_x and dog.dog_x + dog.hitbox_x < chocolate1.coord_x + chocolate1.hitbox_x:
                crash("Oh no! Doggo got sick")
                # Choc2
        if dog.dog_y < chocolate2.coord_y + chocolate2.hitbox_y and dog.dog_y > chocolate2.coord_y or dog.dog_y + dog.hitbox_y > chocolate2.coord_y and dog.dog_y + dog.hitbox_y < chocolate2.coord_y + chocolate2.hitbox_y:
            if dog.dog_x > chocolate2.coord_x and dog.dog_x < chocolate2.coord_x + chocolate2.hitbox_x or dog.dog_x + dog.hitbox_x > chocolate2.coord_x and dog.dog_x + dog.hitbox_x < chocolate2.coord_x + chocolate2.hitbox_x:
                crash("Oh no! Doggo got sick!")
    # Vacuum
        if dog.dog_y < vacuum.coord_y + vacuum.hitbox_y:
            if dog.dog_x > vacuum.coord_x and dog.dog_x < vacuum.coord_x + vacuum.hitbox_x or dog.dog_x + dog.hitbox_x > vacuum.coord_x and dog.dog_x + dog.hitbox_x < vacuum.coord_x + vacuum.hitbox_x:
                crash("Oh no! Doggo got spooked!")
    # Bone
        if dog.dog_y < bone.coord_y + bone.hitbox_y and dog.dog_y > bone.coord_y or dog.dog_y + dog.hitbox_y > bone.coord_y and dog.dog_y + dog.hitbox_y < bone.coord_y + bone.hitbox_y:
            if dog.dog_x > bone.coord_x and dog.dog_x < bone.coord_x + bone.hitbox_x or dog.dog_x + dog.hitbox_x > bone.coord_x and dog.dog_x + dog.hitbox_x < bone.coord_x + bone.hitbox_x:
                bone.coord_y = -10
                bone.coord_x = random.randrange(0, display_width - 25)
                score += 1
                print(score)

        pygame.display.update()
        clock.tick(60)

mainmenu()
selectScreen()
game_loop()
pygame.QUIT()
quit()