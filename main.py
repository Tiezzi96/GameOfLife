import pygame
from pygame.locals import *
from button import ToggleButton, button, OptionBox
from Model import Model
from window import Window
from inputbox import InputBox

# rgb color and font text
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)


print(FULLSCREEN)
pygame.init()
WIDTH = 1900
HEIGHT = 1200
ROWS = 30
COLUMNS = 50
DIM_RECT = 0
MARGIN = 50
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WIN.fill((255, 255, 255))
# aggiunto da me
pygame.display.set_caption("Game of Life")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BRIGHT_RED = (238, 75, 43)
LIGHT_BLUE = (173, 216, 230)


def calculateDimCell(rows, columns):
    global DIM_RECT
    DIM_RECT = (HEIGHT - 2 * MARGIN-200) / rows


# funzione main
# inizializza le componenti dell'interfaccia grafica, la classe model, che gestisce lo stato,
# la classe window che aggiorna l'interfaccia al variare dello stato
# green_button, red_button, blue_button -> pulsanti Play/Stop/Clear del simulation game
# list1, list2 -> pulsanti di selezione della dimensione della griglia e dell stato iniziale
# input_box1 -> sezione per l'inserimento del frame rate

def main(win, width, height):
    run = None
    global ROWS
    global COLUMNS
    global DIM_RECT
    green_button = button((0, 255, 0), MARGIN, height - MARGIN - 100, 230, 50, 'Play')
    red_button = button((255, 0, 0), 1320, height - MARGIN - 100, 230, 50, 'Stop')
    blue_button = button((0, 0, 255), 685, height - MARGIN - 100, 230, 50, 'Clear')
    calculateDimCell(ROWS, COLUMNS)
    input_box1 = InputBox(1600, 500, 140, 32)
    list2 = OptionBox(
        DIM_RECT * COLUMNS + 2 * MARGIN, 800, 160, 40, (150, 150, 150), (100, 200, 255), pygame.font.SysFont(None, 30),
        ["initial state", "white grid"], "State")
    initial_state = list2.active_option

    model = Model(ROWS, COLUMNS, width, height, win, list2.__getattribute__('selected'))
    # inizializzo window
    window = Window(ROWS, COLUMNS, model, DIM_RECT, win)
    list1 = OptionBox(
    DIM_RECT*COLUMNS+2*MARGIN, 200, 160, 40, (150, 150, 150), (100, 200, 255), pygame.font.SysFont(None, 30),
    ["20 x 20", "30 x 30", "50 x 50", "20 x 30", "30 x 50"], "Grid Size", 4)
    history_button = ToggleButton(DIM_RECT*COLUMNS+2*MARGIN, 100, 18)
    dim_grid = list1.active_option
    print("dim_grid: "+str(dim_grid))
    while True:
        dim_grid, initial_state = window.execute(run, dim_grid, initial_state, list1, list2, width, height, history_button,
                                                 input_box1, red_button, green_button, blue_button)


main(WIN, WIDTH, HEIGHT)
