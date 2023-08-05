import pygame
from grid import Grid
from blocks import *

pygame.init

screen = pygame.display.set_mode((300, 600)) #setup w and h of screen
pygame.display.set_caption("Python Tetris") #title

clock = pygame.time.Clock()

game_grid = Grid()

block = LBlock()

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
            SystemExit()

    #Drawing
    screen.fill("pink")
    game_grid.draw(screen)
    block.draw(screen)

    pygame.display.update()
    clock.tick(60) #code will run 60 times a second
