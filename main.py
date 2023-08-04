import pygame

pygame.init

screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Python Tetris")

clock = pygame.time.Clock()

# Game Loop
# 1. Event Handling
# 2. Updating Positions
# 3. Drawing Objects

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            SystemExit()

    pygame.display.update()
    clock.tick(60) #code will run 60 times a second
