import pygame
pygame.init()
BLACK = (0, 0, 0)
MARGIN = 50
DIM_RECT = 0


class Window:
    def __init__(self, rows, cols, model, dim_rect, win):
        self.rows = rows
        self.cols = cols
        self.model = model
        self.dim_rect = dim_rect
        self.win = win

    def draw_grid(self):
        # gap = (width-2*MARGIN) // ROWS
        # gap2 = gap*COLUMNS
        # gap = DIM_RECT
        # gap2 = COLUMNS * DIM_RECT

        '''
        if ROWS >= COLUMNS:
            gap = DIM_RECT
            gap2 = COLUMNS*DIM_RECT
        else:
            gap = DIM_RECT
            gap2 =COLUMNS * DIM_RECT
        '''
        global DIM_RECT
        DIM_RECT = self.dim_rect
        print(self.rows)
        print(self.cols)
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
                if countrow == 49 and countcol == 39 and grid[countrow][countcol].colour == BLACK:
                    print("Hello")
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
                if countrow == 49 and countcol == 39 and grid[countrow][countcol].colour == BLACK:
                    print("Hello")
                spot.draw(self.win)
                countcol += 1

        self.draw_grid()

        pygame.display.update()

