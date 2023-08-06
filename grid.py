import pygame
from colors import Colors

class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = Colors.get_cell_colors()

    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end = " ")
            print()

    def is_inside(self, row, column):
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        return False


    def draw(self, screen):
        # dark krey if cell = 0, green if cell = 1 etc
        for row in range(self.num_rows):
            for cols in range(self.num_cols):
                cell_value = self.grid[row][cols]
                #+1 to add margin, but -1 to stay in 30px
                cell_rect = pygame.Rect(cols*self.cell_size + 1, row*self.cell_size + 1, self.cell_size - 1, self.cell_size - 1) #(x=col, y=row, w=cell_size, h=cell_size)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect) #(surface, color, rect)
