'''
Coding our First Game in PyGame
-
Moving Snake continuously on single press
'''

import pygame
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


# Game Specific Variables
exit_game = False
game_over = False
snake_x = 45            # Initial Position of Snake
snake_y = 55            # Initial Position of Snake
velocity_x = 4
velocity_y = 4
snake_size = 10
fps = 30                # frames per second

clock = pygame.time.Clock()

# Creating a Game Loop
while not exit_game:
    for event in pygame.event.get():                # This gets all the events which a user can perform in a game, like mouse hover, mouse click, pressing a certain key etc.
        print(event)
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = 10
                velocity_y = 0

            if event.key == pygame.K_LEFT:
                velocity_x = - 10
                velocity_y = 0

            if event.key == pygame.K_UP:
                velocity_y = - 10
                velocity_x = 0

            if event.key == pygame.K_DOWN:
                velocity_y = 10
                velocity_x = 0

    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y


    gameWindow.fill(white)                      # Setting background color as white
    pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])                   # Making Head of Snake using Rectangle
    pygame.display.update()                         # Need to update display cause we have made changes to gameWindow
    clock.tick(fps)


pygame.quit()
quit()

