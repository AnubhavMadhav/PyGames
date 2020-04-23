'''
Event Types and Key Press Handling in PyGame
'''

import pygame
pygame.init()
# print(x)              # All 6 pygame modules succesfully imported

# Creating Game Window
gameWindow = pygame.display.set_mode((1200,500))                    # Game Window of 1200x500
pygame.display.set_caption("My First Game")             # Title of the Game, which appears at the top of the window

# Game Specific Variables
exit_game = False
game_over = False


# Creating a Game Loop

while not exit_game:
    for event in pygame.event.get():                # This gets all the events which a user can perform in a game, like mouse hover, mouse click, pressing a certain key etc.
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You have pressed right cursor key")


pygame.quit()
quit()

