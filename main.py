import pygame, sys
from game import Game
from colors import Colors

pygame.init()

title_font = pygame.font.Font(None, 40)

#score text + rectangle for score
score_surface = title_font.render("Score", True, Colors.white)
score_rect = pygame.Rect(320, 55, 170, 60)

#next block + rect for image
next_surface = title_font.render("Next", True, Colors.white)
next_rect = pygame.Rect(320, 215, 170, 180)

#game over
game_over_surface = title_font.render("GAME OVER", True, Colors.white)

screen = pygame.display.set_mode((500, 620)) #setup w and h of screen
pygame.display.set_caption("Python Tetris") #title

clock = pygame.time.Clock()

game = Game()

GAME_UDPATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UDPATE, 200) #trigger game every 200 milliseconds

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
    screen.fill(Colors.pink)
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))

    if game.game_over == True:
        screen.blit(game_over_surface, (320, 450, 50, 50))

    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    game.draw(screen)


    pygame.display.update()
    clock.tick(60) #60 fps
