from enum import Enum

directions = [
    (1, 0), (-1, 0), (0, 1), (0, -1),
    (-1, -1), (1, -1), (-1, 1), (1, 1)
]

class Status(Enum):
    ALIVE = 1
    DEAD = 0

class Cell:

    def __init__(self, status = Status.DEAD):
        self.__status = status
        self.__neighbour_count = 0

    def set_alive(self):
        self.__status = Status.ALIVE

    def set_dead(self):
        self.__status = Status.DEAD

    def get_status(self):
        return self.__status
    
    def set_neighbour(self, n):
        self.__neighbour_count = n

    def add_neighbour(self):
        self.__neighbour_count += 1

    def get_neighbour(self):
        return self.__neighbour_count


class Board:

    def __init__(self, row = 10, column = 10):
        self.__row = row
        self.__column = column
        self.__grid = [[Cell() for i in range(self.__column)] for j in range(self.__row)]

    def check_neighbours(self, rw, clm):
        cell = self.__grid[rw][clm]
        cell.set_neighbour(0)
        for dr, dc in directions:
            nr = rw+dr
            nc = clm+dc
            if nr < 0 or nr >= self.__row or nc < 0 or nc >= self.__column:
                continue
            nghbour_cell = self.__grid[nr][nc]
            if nghbour_cell.get_status() == Status.ALIVE:
                cell.add_neighbour()
        
    def update_neighbours(self):
        for rw in range(self.__row):
            for clm in range(self.__column):
                self.check_neighbours(rw, clm)
                
    
    def update_status(self):
        for rw in range(self.__row):
            for clm in range(self.__column):
                cell = self.__grid[rw][clm]
                if cell.get_status() == Status.DEAD:
                    if cell.get_neighbour() == 3:
                        cell.set_alive()
                else:
                    if cell.get_neighbour() < 2 or cell.get_neighbour() > 3:
                        cell.set_dead()

    def get_row(self): 
        return self.__row
    
    def get_col(self): 
        return self.__column
    
    def get_cell(self, row, col): 
        return self.__grid[row][col]