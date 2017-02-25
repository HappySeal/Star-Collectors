import pygame,time,random,sys

pygame.init()

displayW = 400
displayH = 300

black = (0,0,0)
white = (255,255,255)

gameDisplay = pygame.display.set_mode((displayW,displayH))
pygame.display.set_caption("Begin..")
clock= pygame.time.Clock()

jetImg = pygame.image.load("jet.png")
brickImg = pygame.image.load("brickx16.png")
meteorImg = pygame.image.load("meteorx16.png")
starImg = pygame.image.load("starx8.png")
bigstarImg = pygame.image.load("bigStarx16.png")
backgroundImg = pygame.image.load("background.png")
def bigstar(x,y):
    gameDisplay.blit(bigstarImg,(x,y))
def star(x,y):
    gameDisplay.blit(starImg,(x,y))
def meteor(x,y):
    gameDisplay.blit(meteorImg,(x,y))
def jet(x,y):
    gameDisplay.blit(jetImg,(x,y))
def brick(x,y):
    gameDisplay.blit(brickImg,(x,y))
def background():
    gameDisplay.blit(backgroundImg,(0,0))

def text_objects(text,font):
    textSurface = font.render(text,True,white)
    return textSurface,textSurface.get_rect()

def all_display(text):
    normalText = pygame.font.Font("font.ttf",16)
    TextSurf , TextRect = text_objects(text,normalText)
    TextRect.center = (180,30)
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()

def message_display(text):
    normalText = pygame.font.Font("font.ttf",16)
    TextSurf , TextRect = text_objects(text,normalText)
    TextRect.center = ((displayW/2),(displayH/2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()

    time.sleep(2)

    game_intro()
def all(misses,score):
    a = "Misses : " + str(misses) + "             Score : " + str(score)
    all_display(a)

def crash(score):
    a = "You Died  Your Score Is :" + str(score)
    message_display(a)

def game_intro():
    intro = False

    starX = 150
    starY = 180
    ft = 0

    while not intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:

                    if ft == 0:
                        starX = 150
                        starY = 200
                        ft = 1
                    else:
                        starX = 150
                        starY = 180
                        ft = 0
                if event.key == pygame.K_RETURN:
                    if ft == 0:
                        background()
                        game_loop()
                    else:
                        pygame.quit()
                        quit()

        #Background
        background()
        star(starX,starY)
        largeText = pygame.font.Font("font.TTF",42)
        TextSurf , TextRect = text_objects("STAR COLLECTORS",largeText)
        TextRect.center = (displayW/2,displayH/2)
        gameDisplay.blit(TextSurf,TextRect)

        normalText = pygame.font.Font("font.TTF",16)
        TextSurf , TextRect = text_objects("PLAY",normalText)
        TextRect.center = (200,185)
        gameDisplay.blit(TextSurf,TextRect)

        normalText = pygame.font.Font("font.TTF",16)
        TextSurf , TextRect = text_objects("QUIT",normalText)
        TextRect.center = (200,205)
        gameDisplay.blit(TextSurf,TextRect)




        pygame.display.update()
        clock.tick(30)



def game_loop():
    scorePlayer = 0
    misses = 0

    chance = random.randint(0,100)

    starX = random.randint(0,displayW)
    starY = 0
    starSpeed = 3

    x = (displayW/2)
    y = 268

    x_change = 0
    y_change = 0

    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type ==  pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -3
                elif event.key == pygame.K_RIGHT:
                    x_change = 3
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        background()

        all(misses,scorePlayer)

        jet(x,y)
        if(not scorePlayer > 10):
            starSpeed = 3
        else:
            starSpeed = 3 +(round(scorePlayer/10))

        starY += starSpeed
        if starY > 300 :
            if chance > 25:
                misses+=1
            starY = 0
            starX = random.randint(0,displayW)
            chance = random.randint(0,100)




        if(x + x_change > 0 and x + x_change < 384):
            x += x_change
        else:
            crash(scorePlayer)

        if misses == 3 :
            crash(scorePlayer)

        if x < starX and x > starX-16 and starY  > 268 and starY < 286 :
            if chance > 25 and chance != 100:
                scorePlayer+=1
                if misses != 0:
                    misses-=1
            elif chance == 100:
                scorePlayer+=10
                if misses != 0:
                    misses = 0
            else:
                crash(scorePlayer)
            chance = random.randint(0,100)
            starY = 0
            starX = random.randint(0,displayW)

        if chance > 25 and chance != 100:
            star(starX,starY)
        elif chance <= 25 and chance != 100:
            meteor(starX,starY)
        elif chance == 100:
            bigstar(starX,starY)






        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()

