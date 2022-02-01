import pygame
import sys
from pygame.locals import *
import tkinter
import tkinter.messagebox
from button import ToggleButton, button, OptionBox
from Model import Model
from window import Window
from inputbox import InputBox

COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)


print(FULLSCREEN)
pygame.init()
WIDTH = 1900
HEIGHT = 1200#915
ROWS = 30 #20
COLUMNS = 50
DIM_RECT=0
MARGIN = 50#20
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


def Find_Node(pos, WIDTH):
    interval = (WIDTH-2*MARGIN) / ROWS
    interval_col = (WIDTH-2*MARGIN-(ROWS-COLUMNS)*DIM_RECT)/COLUMNS
    if ROWS > COLUMNS:
        interval = DIM_RECT
        interval_col = (WIDTH-2*MARGIN-(ROWS-COLUMNS)*DIM_RECT)/COLUMNS
        if WIDTH > HEIGHT:
            interval = DIM_RECT
            interval_col = (HEIGHT-2*MARGIN-200-(ROWS-COLUMNS)*DIM_RECT)/COLUMNS
    else:
        interval = DIM_RECT
        interval_col = DIM_RECT
    y, x = pos

    columns = (y-MARGIN) // interval

    rows = (x-MARGIN) // interval_col

    return int(rows), int(columns)


def main(WIN, WIDTH):
    run = None
    global ROWS
    global COLUMNS
    global DIM_RECT
    greenButton = button((0, 255, 0), MARGIN, HEIGHT - MARGIN - 100, 230, 50, 'Play')
    redButton = button((255, 0, 0), 1320, HEIGHT - MARGIN - 100, 230, 50, 'Stop')
    blueButton = button((0, 0, 255), 685, HEIGHT - MARGIN - 100, 230, 50, 'Clear')
    FPS = 1
    calculateDimCell(ROWS, COLUMNS)
    input_box1 = InputBox(1600, 500, 140, 32)
    list2 = OptionBox(
        DIM_RECT * COLUMNS + 2 * MARGIN, 800, 160, 40, (150, 150, 150), (100, 200, 255), pygame.font.SysFont(None, 30),
        ["initial state", "white grid"], "State")
    initial_state = list2.active_option

    model = Model(ROWS, COLUMNS, WIDTH, WIN, list2.__getattribute__('selected'))
    # inizializzo window
    window = Window(ROWS, COLUMNS, model, DIM_RECT, WIN)
    list1 = OptionBox(
    DIM_RECT*COLUMNS+2*MARGIN, 200, 160, 40, (150, 150, 150), (100, 200, 255), pygame.font.SysFont(None, 30),
    ["20 x 20", "30 x 30", "50 x 50", "20 x 30", "30 x 50"], "Grid Size", 4)
    history_button = ToggleButton(DIM_RECT*COLUMNS+2*MARGIN, 100, 18)
    dim_grid = list1.active_option
    print("dim_grid: "+str(dim_grid))
    while True:
        if dim_grid != -1:
            dim = list1.__getattribute__('option_list')[dim_grid]
            l = dim.split()
            ROWS = int(l[0])
            COLUMNS = int(l[2])
            calculateDimCell(ROWS, COLUMNS)
            model = Model(ROWS, COLUMNS, WIDTH, WIN,  list2.__getattribute__('selected'))
            history_button.set_x(DIM_RECT*COLUMNS+2*MARGIN)
            history_button.draw(WIN)
            list1.set_rect_x(DIM_RECT*COLUMNS+2*MARGIN)
            list1.set_selected(dim_grid)
            list1.draw(WIN)
            list2.set_rect_x(DIM_RECT*COLUMNS+2*MARGIN)
            list2.draw(WIN)
            input_box1.set_rect_x(DIM_RECT * COLUMNS + 2 * MARGIN)
            input_box1.draw(WIN, FPS)
            # inizializzo window
            window = Window(ROWS, COLUMNS, model, DIM_RECT, WIN)
            window.update_display()
            pygame.display.flip()
            dim_grid = -1
        if initial_state != -1:
            model = Model(ROWS, COLUMNS, WIDTH, WIN, initial_state)
            window = Window(ROWS, COLUMNS, model, DIM_RECT, WIN)
            window.update_display()
            pygame.display.flip()
            dim_grid = -1
        pygame.time.delay(50)
        WIN.fill((255, 255, 255))
        greenButton.draw(WIN, (0, 0, 0))
        redButton.draw(WIN, (0, 0, 0))
        blueButton.draw(WIN, (0, 0, 0))
        history_button.draw(WIN)
        input_box1.draw(WIN, FPS)
        list1.draw(WIN)
        list2.draw(WIN)
        event_list = pygame.event.get()##stops cpu dying
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                input_box1.handle_event(event)
                fps = input_box1.__getattribute__('text_insert')
                if fps != '' and fps.isdigit():
                    print("FPS is integer")
                    FPS = int(fps)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                input_box1.handle_event(event)

                if greenButton.isOver(pos):
                    run = True
                elif redButton.isOver(pos):
                    run = False
                elif blueButton.isOver(pos):
                    model = Model(ROWS, COLUMNS, WIDTH, WIN,  list2.__getattribute__('selected'))
                    window = Window(ROWS, COLUMNS, model, DIM_RECT, WIN)
                elif history_button.isOver(pos):
                    history_button.draw(WIN)
                    window.update_display_history_map()
                elif pos[0] < MARGIN or pos[0] > DIM_RECT*COLUMNS+MARGIN:
                    break
                elif pos[1] < MARGIN or pos[1] > DIM_RECT*ROWS+MARGIN:
                    break
                else:
                    oi = (WIDTH-MARGIN-((WIDTH-2*MARGIN)/ROWS)*(ROWS-COLUMNS))
                    row, col = Find_Node(pos, WIDTH)
                    model.setstatecell(row, col)
            clock = pygame.time.Clock()
            while run:
                clock.tick(FPS)
                event_list2 = pygame.event.get()
                for event in event_list2:

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        posM = pygame.mouse.get_pos()
                        if redButton.isOver(posM):
                            run = False
                            break
                        elif blueButton.isOver(posM):
                            run = False
                            model = Model(ROWS, COLUMNS, WIDTH, WIN,  list2.__getattribute__('selected'))
                            window = Window(ROWS, COLUMNS, model, DIM_RECT, WIN)
                            break
                        elif greenButton.isOver(posM):
                            tkinter.Tk().wm_withdraw()  # to hide the main window
                            tkinter.messagebox.showinfo("Play Disabled", "Press Stop for modify grid")

                if run is False:
                    break
                model.update_grid()
                model.update_historyMap()
                window.update_display()
        if history_button.colour != BRIGHT_RED:
            window.update_display()
        else:
            window.update_display_history_map()
        section_list = list1.update(event_list)
        section_list2 = list2.update(event_list)
        input_box1.update()
        input_box1.draw(WIN, FPS)
        dim_grid = section_list
        initial_state = section_list2


main(WIN, WIDTH)
