import pygame

pygame.init()
WIDTH = 1900#800
HEIGHT = 1200#915
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
MARGIN = 50


class Node:
    def __init__(self, row, col, width, model, color=WHITE, occupied=None):
        self.row = row

        self.col = col

        self.width = width

        self.x = int(MARGIN + col * width)

        self.y = int(MARGIN + row * width)

        self.colour = color

        self.occupied = occupied

        self.time_of_life = 0

        self.model = model

    def draw(self, win):
        if self.model.rows > self.model.cols and HEIGHT >= WIDTH:
            pygame.draw.rect(win, self.colour, pygame.Rect(self.x, self.y, (WIDTH - 2 * MARGIN) / self.model.rows, (WIDTH - 2 * MARGIN) / self.model.rows))
        elif self.model.rows > self.model.cols and WIDTH > HEIGHT:
            pygame.draw.rect(win, self.colour, pygame.Rect(self.x, self.y, (HEIGHT - 2 * MARGIN-200) / self.model.rows, (HEIGHT - 2 * MARGIN-200) / self.model.rows))
        elif self.model.rows <= self.model.cols and HEIGHT >= WIDTH:
            pygame.draw.rect(win, self.colour,
                           pygame.Rect(self.x, self.y, (WIDTH - 2 * MARGIN) / self.model.cols, (WIDTH - 2 * MARGIN) / self.model.cols))
        elif self.model.rows <= self.model.cols and WIDTH > HEIGHT and WIDTH-HEIGHT >= 700:
            pygame.draw.rect(win, self.colour,
                             pygame.Rect(self.x, self.y, (HEIGHT - 2 * MARGIN - 200) / self.model.rows,
                                         (HEIGHT - 2 * MARGIN - 200) / self.model.rows))
        else:
            pygame.draw.rect(win, self.colour, pygame.Rect(self.x, self.y, (HEIGHT - 2 * MARGIN - 200) / self.model.cols,
                                                           (HEIGHT - 2 * MARGIN - 200) / self.model.cols))
