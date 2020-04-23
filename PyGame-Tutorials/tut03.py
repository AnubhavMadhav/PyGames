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

while not exit_game:              # This is an infinite loop for now
    pass

pygame.quit()
quit()