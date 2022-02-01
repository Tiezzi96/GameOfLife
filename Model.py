from typing import Any

import pygame
import time
from Node import Node
pygame.init()
WIDTH = 1900
HEIGHT = 1200
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
MARGIN = 50
ROWS = 30
COLUMNS = 50

BRIGHT_RED = (238, 75, 43)
LIGHT_BLUE = (173, 216, 230)


class Model:
    def __init__(self, rows, columns, width, win, state):
        global ROWS
        global COLUMNS
        ROWS = rows
        COLUMNS = columns
        self.dim_rect = self.calculateDimCell(rows)
        self.rows = rows
        self.cols = columns
        self.width = width
        self.initial_state = state
        self.grid = self.make_grid(self.rows, self.cols, self.initial_state)
        self.gridHistoryMap = self.make_grid_history(self.rows, self.cols, self.initial_state)
        self.window = win

    def calculateDimCell(self, rows):
        dim_rect = (HEIGHT - 2 * MARGIN - 200) / rows
        return dim_rect

    def make_grid(self, rows, columns, initial_state):
        grid = []
        if initial_state == 1:
            for i in range(rows):
                grid.append([])
                for j in range(columns):
                    if i == 49 and j == 39:
                        print("Hello")
                    node = Node(i, j, self.dim_rect, self)

                    grid[i].append(node)
        else:
            for i in range(rows):
                row = rows//2
                col = columns//2
                color = BLACK
                neighbor = [[row, col-1], [row, col+1], [row+1, col], [row+1, col-1],
                            [row+1, col+1], [row-1, col-1], [row-1, col], [row-1, col+1]]
                grid.append([])
                for j in range(columns):
                    if [i, j] in neighbor:
                        node = Node(i, j, self.dim_rect, self, color)
                    else:
                        node = Node(i, j, self.dim_rect, self)
                    grid[i].append(node)

        return grid

    def make_grid_history(self, rows, columns, initial_state):
        grid = []
        if initial_state == 1:
            for i in range(rows):
                grid.append([])
                for j in range(columns):
                    if i == 49 and j == 39:
                        print("Hello")
                    node = Node(i, j, self.dim_rect, self)

                    grid[i].append(node)
        else:
            for i in range(rows):
                row = rows//2
                col = columns//2
                color = LIGHT_BLUE
                neighbor = [[row, col-1], [row, col+1], [row+1, col], [row+1, col-1],
                            [row+1, col+1], [row-1, col-1], [row-1, col], [row-1, col+1]]
                grid.append([])
                for j in range(columns):
                    if [i, j] in neighbor:
                        node = Node(i, j, self.dim_rect, self, color, 1)
                    else:
                        node = Node(i, j, self.dim_rect, self)
                    grid[i].append(node)

        return grid

    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)

    def neighbour(self, tile):
        row, col = tile.row, tile.col
        print("ciao")
        if tile.colour is BLACK:
            print("Row e col: " + str(row) + " " + str(col))
        # time.sleep(1)
        neighbours = [[row - 1, col - 1], [row - 1, col], [row - 1, col + 1],
                      [row, col - 1], [row, col + 1],
                      [row + 1, col - 1], [row + 1, col], [row + 1, col + 1], ]

        actual = []

        for i in neighbours:
            row, col = i

            if 0 <= row <= (self.rows - 1) and 0 <= col <= (self.cols - 1):
                actual.append(i)
        # print(row, col, actual)
        print(actual)
        return actual

    def update_grid(self):
        newgrid = []
        countrow = 0
        countcol = 0
        for row in self.grid:
            countcol = 0
            for tile in row:
                if countrow == 28 and countcol == 18:
                    print("Yes")
                neighbours = self.neighbour(tile)
                count = 0
                for i in neighbours:
                    row, col = i
                    if self.grid[row][col].__getattribute__('colour') == BLACK:
                        count += 1
                    print(self.grid[row][col].__getattribute__('colour'))

                if tile.colour == BLACK:
                    print("count " + str(count))
                    if count == 2 or count == 3:
                        newgrid.append(BLACK)
                    else:
                        newgrid.append(WHITE)
                else:
                    print("count " + str(count))
                    if count == 3:
                        print("count is 3")
                        newgrid.append(BLACK)
                    else:
                        newgrid.append(WHITE)
                countcol += 1
            countrow += 1
        print("oi" + str(newgrid))
        index = 0

        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                self.grid[i][j].colour = newgrid[index]
                index += 1

        return newgrid

    def update_historyMap(self):
        newgrid = []
        countrow = 0
        countcol = 0
        for row in self.gridHistoryMap:
            countcol = 0
            for tile in row:
                neighbours = self.neighbour(tile)
                count = 0
                for i in neighbours:
                    row, col = i
                    if self.gridHistoryMap[row][col].__getattribute__('colour') != WHITE:
                        count += 1
                    print(self.gridHistoryMap[row][col].__getattribute__('colour'))

                if tile.colour != WHITE:
                    print("count " + str(count))
                    if count == 2 or count == 3:
                        newgrid.append([tile.colour, tile.occupied + 1])
                    else:
                        newgrid.append([WHITE, 0])

                else:
                    print("count " + str(count))
                    if count == 3:
                        print("count is 3")
                        newgrid.append([LIGHT_BLUE, 1])
                    else:
                        newgrid.append([WHITE, 0])
                if newgrid[len(newgrid) - 1][1] % 3 == 0 and newgrid[len(newgrid) - 1][0] != WHITE:
                    print("LIGHT_BLUE[1]: " + str(newgrid[len(newgrid) - 1][0][1]))
                    g = newgrid[len(newgrid) - 1][0][1] - 4
                    b = newgrid[len(newgrid) - 1][0][2] - 4
                    if g < 0:
                        g = 0
                    if b < 0:
                        b = 0
                    newgrid[len(newgrid) - 1][0] = (newgrid[len(newgrid) - 1][0][0], g, b)

                countcol += 1
            countrow += 1

        index = 0

        for i in range(len(self.gridHistoryMap)):
            for j in range(len(self.gridHistoryMap[0])):
                self.gridHistoryMap[i][j].colour = newgrid[index][0]
                self.gridHistoryMap[i][j].occupied = newgrid[index][1]
                index += 1

        return newgrid

    def setstatecell(self, row, col):
        if self.grid[row][col].__getattribute__('colour') == WHITE:
            self.grid[row][col].__setattr__('colour', BLACK)
            self.gridHistoryMap[row][col].__setattr__('colour', LIGHT_BLUE)
            self.gridHistoryMap[row][col].__setattr__('occupied', 1)
            # time
            self.grid[row][col].__setattr__('time_of_life', time.time())
            # end time
            print(self.grid[row][col].__getattribute__('x'))
            print(self.grid[row][col].__getattribute__('colour'))
        elif self.grid[row][col].__getattribute__('colour') == BLACK:
            # time
            self.grid[row][col].__setattr__('time_of_life', time.time()-self.grid[row][col].__getattribute__('time_of_life'))
            # end time
            self.grid[row][col].__setattr__('colour', WHITE)
            self.gridHistoryMap[row][col].__setattr__('colour', WHITE)
            self.gridHistoryMap[row][col].__setattr__('occupied', 0)
            print(self.grid[row][col].__getattribute__('colour'))