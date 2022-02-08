import pygame
import tkinter
from tkinter import messagebox
import sys
pygame.init()
BRIGHT_RED = (238, 75, 43)
BLACK = (0, 0, 0)
MARGIN = 50
DIM_RECT = 0
HEIGHT = 1200


# Window -> gestisce l'aggiornamento dell'interfaccia al variare dello stato.
# update_display() -> aggiorna l'interfaccia a seguito della variazione di stato del modello
# update_display_history_map() -> aggiorna l'interfaccia mostrando l'history map
# Run() -> aggiorna l'interfaccia durante durante la fase di gioco
# execute() -> avvia l'interfaccia di gioco una volta inizializzate le componenti nella funzione main del file main.py
# Find_Node() -> individua la cella con cui l'utente interagisce in base alle coordinate del cursore

class Window:
    def __init__(self, rows, cols, model, dim_rect, win):
        self.rows = rows
        self.cols = cols
        self.model = model
        self.dim_rect = dim_rect
        self.win = win

    def draw_grid(self):
        global DIM_RECT
        DIM_RECT = self.dim_rect
        for i in range(self.rows + 1):
            pygame.draw.line(self.win, BLACK, (0 + MARGIN, i * DIM_RECT + MARGIN),
                             (MARGIN + self.cols * DIM_RECT, i * DIM_RECT + MARGIN))

            for j in range(self.cols + 1):
                pygame.draw.line(self.win, BLACK, (j * DIM_RECT + MARGIN, 0 + MARGIN),
                                 (j * DIM_RECT + MARGIN, self.rows * DIM_RECT + MARGIN))

    def update_display(self):
        countrow = 0
        grid = self.model.__getattribute__('grid')
        for row in grid:
            countrow += 1
            countcol = 0
            for spot in row:
                spot.draw(self.win)
                countcol += 1

        self.draw_grid()

        pygame.display.update()

    def update_display_history_map(self):
        countrow = 0
        grid = self.model.__getattribute__('gridHistoryMap')
        for row in grid:
            countrow += 1
            countcol = 0
            for spot in row:
                spot.draw(self.win)
                countcol += 1

        self.draw_grid()

        pygame.display.update()

    def Run(self, run, width, height, clock, green_button,  blue_button, red_button, list2):
        clock.tick(self.model.__getattribute__('fps'))
        event_list2 = pygame.event.get()
        for event in event_list2:
            if event.type == pygame.MOUSEBUTTONDOWN:
                posM = pygame.mouse.get_pos()
                if red_button.isOver(posM):
                    run = False
                    break
                elif blue_button.isOver(posM):
                    run = False
                    self.model.__init__(self.rows, self.cols, width, height, self.win, list2.__getattribute__('selected'),
                                        self.model.__getattribute__('fps'))
                    self.__init__(self.rows, self.cols, self.model, self.dim_rect, self.win)
                    break
                elif green_button.isOver(posM):
                    tkinter.Tk().wm_withdraw()  # to hide the main window
                    tkinter.messagebox.showinfo("Play Disabled", "Press Stop for modify grid")

        if run is False:
            return run
        self.model.update_grid()
        self.model.update_historyMap()
        self.update_display()
        return run

    # metodo execute: gestisce l'esecuzione del gioco. Restituisce il valore della griglia
    def execute(self, run, dim_grid, initial_state, list1, list2, width, height, history_button, input_box1, red_button,
                green_button, blue_button):
        if dim_grid != -1:
            dim = list1.__getattribute__('option_list')[dim_grid]
            l = dim.split()
            self.rows = int(l[0])
            self.cols = int(l[2])
            self.dim_rect = self.model.calculateDimCell(self.rows)
            self.model.__init__(self.rows, self.cols, width, height, self.win,  list2.__getattribute__('selected'), self.model.__getattribute__('fps'))
            history_button.set_x(self.dim_rect*self.cols+2*MARGIN)
            history_button.draw(self.win)
            list1.set_rect_x(self.dim_rect*self.cols+2*MARGIN)
            list1.set_selected(dim_grid)
            list1.draw(self.win)
            list2.set_rect_x(self.dim_rect*self.cols+2*MARGIN)
            list2.draw(self.win)
            input_box1.set_rect_x(self.dim_rect * self.cols + 2 * MARGIN)
            input_box1.draw(self.win, self.model.__getattribute__('fps'))
            # inizializzo window
            self.__init__(self.rows, self.cols, self.model, self.dim_rect, self.win)
            self.update_display()
            pygame.display.flip()
            dim_grid = -1
        if initial_state != -1:
            self.model.__init__(self.rows, self.cols, width, height, self.win, initial_state, self.model.__getattribute__('fps'))
            self.__init__(self.rows, self.cols, self.model, self.dim_rect, self.win)
            self.update_display()
            pygame.display.flip()
            initial_state = -1
        pygame.time.delay(50)
        self.win.fill((255, 255, 255))
        green_button.draw(self.win, (0, 0, 0))
        red_button.draw(self.win, (0, 0, 0))
        blue_button.draw(self.win, (0, 0, 0))
        history_button.draw(self.win)
        input_box1.draw(self.win, self.model.__getattribute__('fps'))
        list1.draw(self.win)
        list2.draw(self.win)
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                input_box1.handle_event(event)
                fps = input_box1.__getattribute__('text_insert')
                if fps != '' and fps.isdigit():
                    self.model.__setattr__('fps', int(fps))
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                input_box1.handle_event(event)
                if green_button.isOver(pos):
                    run = True
                elif red_button.isOver(pos):
                    run = False
                elif blue_button.isOver(pos):
                    self.model.__init__(self.rows, self.cols, width, height, self.win,  list2.__getattribute__('selected'), self.model.__getattribute__('fps'))
                    self.__init__(self.rows, self.cols, self.model, self.dim_rect, self.win)
                elif history_button.isOver(pos):
                    history_button.draw(self.win)
                    self.update_display_history_map()
                elif pos[0] < MARGIN or pos[0] > self.dim_rect*self.cols+MARGIN:
                    break
                elif pos[1] < MARGIN or pos[1] > self.dim_rect*self.rows+MARGIN:
                    break
                else:
                    row, col = self.Find_Node(pos, width)
                    self.model.setstatecell(row, col)
            clock = pygame.time.Clock()
            while run:
                run = self.Run(run, width, height, clock, green_button, blue_button, red_button, list2)
        if history_button.colour != BRIGHT_RED:
            self.update_display()
        else:
            self.update_display_history_map()
        section_list = list1.update(event_list)
        section_list2 = list2.update(event_list)
        input_box1.update()
        input_box1.draw(self.win, self.model.__getattribute__('fps'))
        dim_grid = section_list
        initial_state = section_list2
        return dim_grid, initial_state

    def Find_Node(self, pos, width):
        interval_col = (width - 2 * MARGIN - (self.rows - self.cols) * self.dim_rect) / self.cols
        if self.rows > self.cols:
            interval = self.dim_rect
            interval_col = (width - 2 * MARGIN - (self.rows - self.cols) * self.dim_rect) / self.cols
            if width > HEIGHT:
                interval = self.dim_rect
                interval_col = (HEIGHT - 2 * MARGIN - 200 - (self.rows - self.cols) * self.dim_rect) / self.cols
        else:
            interval = self.dim_rect
            interval_col = self.dim_rect
        y, x = pos

        columns = (y - MARGIN) // interval

        rows = (x - MARGIN) // interval_col

        return int(rows), int(columns)
