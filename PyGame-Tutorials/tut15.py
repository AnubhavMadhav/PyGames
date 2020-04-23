'''
Coding our First Game in PyGame
-
Handling Game Over and Collision
'''

import pygame
import random
pygame.init()
# print(x)              # All 6 pygame modules successfully imported

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)


# Creating Game Window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))                    # Game Window of 1200x500
pygame.display.set_caption("Snake - by Anubhav Madhav")             # Title of the Game, which appears at the top of the window
pygame.display.update()                 # We need to update our display each and everytime we make a change



clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 55)
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])




def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


# Creating a Game Loop
def gameloop():
    # Game Specific Variables
    exit_game = False
    game_over = False
    snake_x = 45  # Initial Position of Snake
    snake_y = 55  # Initial Position of Snake
    snake_size = 30
    init_velocity = 5
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    food_size = 30
    score = 0
    fps = 30  # frames per second

    snk_list = []
    snk_length = 1

    while not exit_game:

        if game_over:
            gameWindow.fill(white)
            text_screen("Game Over!! Press Enter to Continue", red, 100, 250)

            for event in pygame.event.get():                # This gets all the events which a user can perform in a game, like mouse hover, mouse click, pressing a certain key etc.
                # print(event)
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()


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

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y


            if abs(snake_x - food_x)<6  and abs(snake_y - food_y)<6:                # condition when snake eats the food
                score += 1
                print("Score: ", score*10 )
                food_x = random.randint(20, screen_width / 2)               # to change the position of food after eating
                food_y = random.randint(20, screen_height / 2)
                snk_length += 5

            gameWindow.fill(white)                      # Setting background color as white

            pygame.draw.rect(gameWindow, red, [food_x, food_y, food_size, food_size])                   # Making Food for Snake using Rectangle

            text_screen("Score: " + str(score * 10), red, 5, 5)

            head = []                           # for the starting of the game
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over  = True


            if snake_x<0 or snake_x>screen_height or snake_y<0 or snake_y>screen_height:
                game_over = True
                # print("Game Over!!")

            # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])                   # Making Head of Snake using Rectangle
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()                         # Need to update display cause we have made changes to gameWindow
        clock.tick(fps)


    pygame.quit()
    quit()

gameloop()