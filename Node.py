import pygame
pygame.init()
WIDTH = 1900
HEIGHT = 1200
MARGIN = 50

# RGB Color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_BLUE = (173, 216, 230)

# Node -> alloca ogni cella appartenente alla griglia e ne gestisce l'interfaccia
# al variare dello stato
# row -> riga di appartenenza
# col -> colonna di appartenenza
# x,y -> coordinate della cella
# width -> dimensione della cella
# occupied -> indica la durata della vita, 0 = dead cell
# color_state -> indica lo stato della cella
# colour -> colore della cella
# model -> gestisce lo stato del simulation game


class Node:
    def __init__(self, row, col, width, model, color_state=255, color=WHITE, occupied=0):
        self.row = row

        self.col = col

        self.width = width

        self.x = int(MARGIN + col * width)

        self.y = int(MARGIN + row * width)

        self.color_state = color_state

        self.colour = color

        self.occupied = occupied

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

    # colour_state -> setta il colore della cella in base al suo stato

    def colour_state(self):
        if self.color_state == 0:
            self.colour = BLACK
        elif self.color_state == 255:
            self.colour = WHITE

    # colour_state_history -> setta il colore della cella appartenente a history map

    def colour_state_history(self):
        if self.color_state == 0:
            self.colour = LIGHT_BLUE
        elif self.color_state == 255 and self.occupied is not None and self.occupied == 0:
            self.colour = WHITE
        else:
            print(LIGHT_BLUE[1])
            green = LIGHT_BLUE[1] - self.color_state
            blue = LIGHT_BLUE[2] - self.color_state
            if green < 0:
                green = 0
            if blue < 0:
                blue = 0
            self.colour = (LIGHT_BLUE[0], green, blue)
