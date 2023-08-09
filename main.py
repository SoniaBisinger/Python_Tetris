import pygame, sys
from game import Game

pygame.init
pink = (255, 162, 214)

screen = pygame.display.set_mode((300, 600)) #setup w and h of screen
pygame.display.set_caption("Python Tetris") #title

clock = pygame.time.Clock()

game = Game()

GAME_UDPATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UDPATE, 20) #trigger game every 200 milliseconds

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

        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotation()
        if event.type == GAME_UDPATE and game.game_over == False:
            game.move_down()

    #Drawing
    screen.fill(pink)
    game.draw(screen)


    pygame.display.update()
    clock.tick(60) #60 fps
