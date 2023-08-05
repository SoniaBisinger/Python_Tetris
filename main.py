import pygame, sys

from game import Game

pygame.init
pink = (255, 162, 214)

screen = pygame.display.set_mode((300, 600)) #setup w and h of screen
pygame.display.set_caption("Python Tetris") #title

clock = pygame.time.Clock()

game = Game()

#random test for our grid class
# game_grid.grid[0][0] = 1
# game_grid.grid[3][5] = 4
# game_grid.grid[17][8] = 7

# Game Loop
# 1. Event Handling
# 2. Updating Positions
# 3. Drawing Objects

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Drawing
    screen.fill(pink)
    game.draw(screen)


    pygame.display.update()
    clock.tick(60) #code will run 60 times a second
