'''
Coding our First Game in PyGame
-
Adding Music and Background Image in PyGame
'''

import pygame
import random
import os
pygame.init()
pygame.mixer.init()
# print(x)              # All 6 pygame modules successfully imported

# Colors
white = (255, 255, 255)
red = (255, 69, 0)
black = (0, 0, 0)


# Creating Game Window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))                    # Game Window of 1200x500
pygame.display.set_caption("Snake - by Anubhav Madhav")             # Title of the Game, which appears at the top of the window
pygame.display.update()                 # We need to update our display each and everytime we make a change

# Background Image
bgimg = pygame.image.load("bgimg.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()            # convert alpha do not let the loading of image make delay in game
homeimg = pygame.image.load("home.jpg")
homeimg = pygame.transform.scale(homeimg, (screen_width, screen_height)).convert_alpha()            # convert alpha do not let the loading of image make delay in game

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 55)
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])




def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


def welcome():                      # For Home Screen
    exit_game = False
    while not exit_game:
        gameWindow.fill((233, 220, 229))
        gameWindow.blit(homeimg, (0, 0))
        text_screen("Welcome to Snake", black, 260, 150)
        text_screen("Developed by Anubhav Madhav", black, 170, 200)
        text_screen("Press Space Bar to Play", black, 220, 350)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()

        pygame.display.update()
        clock.tick(30)                          # hardcoded 'fps' because 'fps' is local variable of gameloop(), therefore we cannot use it in welcome()


# Creating a Game Loop
def gameloop():
    pygame.mixer.music.load('back.mp3')
    pygame.mixer.music.play()
    # Game Specific Variables
    exit_game = False
    game_over = False
    snake_x = 90  # Initial Position of Snake
    snake_y = 90  # Initial Position of Snake
    snake_size = 30
    init_velocity = 5
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(80, 80)
    food_y = random.randint(80, 80)
    food_size = 30
    score = 0
    fps = 30  # frames per second

    snk_list = []
    snk_length = 1

    if (not os.path.exists("highscore.txt")):               # auto-generate of "highscore" file, if it doesn't exists
        with open("highscore.txt", "w") as f:
            f.write("0")


    with open("highscore.txt", "r") as f:
        hiscore = f.read()

    while not exit_game:

        if game_over:
            gameWindow.fill(white)
            text_screen("Game Over!! Press Enter to Continue", red, 100, 250)
            with open("highscore.txt", "w") as f:
                f.write(str(hiscore))



            for event in pygame.event.get():                # This gets all the events which a user can perform in a game, like mouse hover, mouse click, pressing a certain key etc.
                # print(event)
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()


        else:

            for event in pygame.event.get():                # This gets all the events which a user can perform in a game, like mouse hover, mouse click, pressing a certain key etc.
                # print(event)
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_q:                 # cheatcode
                        score += 10

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y


            if abs(snake_x - food_x)<9  and abs(snake_y - food_y)<9:                # condition when snake eats the food
                score += 10
                # print("Score: ", score )
                food_x = random.randint(60, screen_width / 2)               # to change the position of food after eating
                food_y = random.randint(60, screen_height / 2)
                snk_length += 5
                # pygame.mixer.music.load('beep-small.mp3')         # doesn't sounds nice
                # pygame.mixer.music.play()

                if score>int(hiscore):
                    hiscore = score

            gameWindow.fill(white)                      # Setting background color as white
            gameWindow.blit(bgimg, (0, 0))
            pygame.draw.rect(gameWindow, red, [food_x, food_y, food_size, food_size])                   # Making Food for Snake using Rectangle

            text_screen("Score: " + str(score ) + "   HighScore: " + str(hiscore), red, 5, 5)

            head = []                           # for the starting of the game
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over  = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

            if snake_x<60 or snake_x>screen_width-90 or snake_y<50 or snake_y>screen_height-80:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
                # print("Game Over!!")

            # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])                   # Making Head of Snake using Rectangle
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()                         # Need to update display cause we have made changes to gameWindow
        clock.tick(fps)


    pygame.quit()
    quit()

welcome()