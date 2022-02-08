from typing import Any
import pygame
from Node import Node
pygame.init()
MARGIN = 50

# Model -> classe che gestisce lo stato del simulation game.
# initial_state -> stato al momento dell'inizializzazione
# fps -> frame rate
# height, width -> dimensione della finestra
# window -> finestra
# dim_rect -> dimensione di ogni cella della griglia


class Model:
    def __init__(self, rows, columns, width, height, win, state, fps=1):
        self.height = height
        self.dim_rect = self.calculateDimCell(rows)
        self.rows = rows
        self.cols = columns
        self.width = width
        self.initial_state = state
        self.grid = self.make_grid()
        self.gridHistoryMap = self.make_grid_history()
        self.window = win
        self.fps = fps

    # calculateDimCell -> calcola la dimensione delle celle

    def calculateDimCell(self, rows):
        dim_rect = (self.height - 2 * MARGIN - 200) / rows
        return dim_rect

    # make_grid -> genera la griglia
    # rows-> righe della griglia
    # cols -> colonne della griglia
    def make_grid(self):
        grid = []
        if self.initial_state == 1:
            for i in range(self.rows):
                grid.append([])
                for j in range(self.cols):
                    node = Node(i, j, self.dim_rect, self)

                    grid[i].append(node)
        else:
            for i in range(self.rows):
                row = self.rows // 2
                col = self.cols // 2
                color = 0
                neighbor = [[row, col-1], [row, col+1], [row+1, col], [row+1, col-1],
                            [row+1, col+1], [row-1, col-1], [row-1, col], [row-1, col+1]]
                grid.append([])
                for j in range(self.cols):
                    if [i, j] in neighbor:
                        node = Node(i, j, self.dim_rect, self, color)
                        node.colour_state()
                    else:
                        node = Node(i, j, self.dim_rect, self)
                    grid[i].append(node)

        return grid

    # make_grid_history->metodo analogo a make_grid() per la creazione della history map

    def make_grid_history(self):
        grid = []
        if self.initial_state == 1:
            for i in range(self.rows):
                grid.append([])
                for j in range(self.cols):
                    node = Node(i, j, self.dim_rect, self)
                    grid[i].append(node)
        else:
            for i in range(self.rows):
                row = self.rows // 2
                col = self.cols // 2
                color = 0
                neighbor = [[row, col-1], [row, col+1], [row+1, col], [row+1, col-1],
                            [row+1, col+1], [row-1, col-1], [row-1, col], [row-1, col+1]]
                grid.append([])
                for j in range(self.cols):
                    if [i, j] in neighbor:
                        node = Node(i, j, self.dim_rect, self, color)
                        node.__setattr__('occupied', 0)
                        node.colour_state_history()
                    else:
                        node = Node(i, j, self.dim_rect, self)
                    grid[i].append(node)

        return grid

    def __getattribute__(self, name: str) -> Any:
        return super().__getattribute__(name)

    # neighbour -> individua le celle vicine alla cella tile
    # ne restituisce la lista
    def neighbour(self, tile):
        row, col = tile.row, tile.col
        neighbours = [[row - 1, col - 1], [row - 1, col], [row - 1, col + 1],
                      [row, col - 1], [row, col + 1],
                      [row + 1, col - 1], [row + 1, col], [row + 1, col + 1], ]

        actual = []

        for i in neighbours:
            row, col = i

            if 0 <= row <= (self.rows - 1) and 0 <= col <= (self.cols - 1):
                actual.append(i)
        return actual

    # update_grid -> esegue l'aggiornamento dello stato del simulation game
    # newgrid.append(255) -> WHITE, dead cell
    # newgrid.append(0) -> BLACK, alive cell
    def update_grid(self):
        newgrid = []
        countrow = 0
        countcol = 0
        for row in self.grid:
            countcol = 0
            for tile in row:
                neighbours = self.neighbour(tile)
                count = 0
                for i in neighbours:
                    row, col = i
                    if self.grid[row][col].__getattribute__('color_state') == 0:
                        count += 1

                if tile.color_state == 0:
                    print("count " + str(count))
                    if count == 2 or count == 3:
                        newgrid.append(0)
                    else:
                        newgrid.append(255)
                else:
                    print("count " + str(count))
                    if count == 3:
                        print("count is 3")
                        newgrid.append(0)
                    else:
                        newgrid.append(255)
                countcol += 1
            countrow += 1
        print("oi" + str(newgrid))
        index = 0

        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                self.grid[i][j].color_state = newgrid[index]
                self.grid[i][j].colour_state()
                index += 1

        return newgrid

    # update_historyMap -> esegue l'aggiornamento dello stato dell'history map
    # newgrid[index][0] -> contiene il codice che indica il colore della cella:
    # 255 -> WHITE, dead cell
    # 0 -> LIGHT_BLUE, just born cell
    # valore differente, -> old cell, different color
    # newgrid[index][1] -> indica lo stato della cella
    # 0 -> dead cell
    # 1 -> alive cell
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
                    if self.gridHistoryMap[row][col].__getattribute__('color_state') != 255:
                        count += 1

                if tile.color_state != 255:
                    print("count " + str(count))
                    if count == 2 or count == 3:
                        newgrid.append([tile.color_state, tile.occupied + 1])
                    else:
                        newgrid.append([255, 0])

                else:
                    print("count " + str(count))
                    if count == 3:
                        print("count is 3")
                        newgrid.append([0, 1])
                    else:
                        newgrid.append([255, 0])
                if newgrid[len(newgrid) - 1][1] % 3 == 0 and newgrid[len(newgrid) - 1][0] != 255:
                    newgrid[len(newgrid) - 1][0] += 4
                countcol += 1
            countrow += 1

        index = 0

        for i in range(len(self.gridHistoryMap)):
            for j in range(len(self.gridHistoryMap[0])):
                self.gridHistoryMap[i][j].color_state = newgrid[index][0]
                self.gridHistoryMap[i][j].occupied = newgrid[index][1]
                self.gridHistoryMap[i][j].colour_state_history()
                index += 1

        return newgrid

    # setstatecell -> modifica lo stato della cella secondo l'interazione dell'utente col la griglia
    # colour_state() -> funzione per aggiornare il colore della cella in base al cambiamento di stato avvenuto
    # colour_state_history() -> funzione analoga a colour_state(), aggiorna l'interfaccia dell'history map

    def setstatecell(self, row, col):
        if self.grid[row][col].__getattribute__('color_state') == 255:
            self.grid[row][col].__setattr__('color_state', 0)
            self.grid[row][col].colour_state()
            self.gridHistoryMap[row][col].__setattr__('color_state', 0)
            self.gridHistoryMap[row][col].__setattr__('occupied', 1)
            self.gridHistoryMap[row][col].colour_state_history()
        elif self.grid[row][col].__getattribute__('color_state') == 0:
            self.grid[row][col].__setattr__('color_state', 255)
            self.grid[row][col].colour_state()
            self.gridHistoryMap[row][col].__setattr__('color_state', 255)
            self.gridHistoryMap[row][col].__setattr__('occupied', 0)
            self.gridHistoryMap[row][col].colour_state_history()
