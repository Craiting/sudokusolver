from puzzle import Puzzle
from cell import Cell


class Puzzle9x9(Puzzle):

    def __init__(self):
        super(Puzzle9x9, self).__init__()
        self.size = 9

    def create_cell(self, row, col, value):
        possible_values = [1,2,3,4,5,6,7,8,9]
        cell = Cell(row, col, value, possible_values)
        if row <= 2 and col <= 2:
            cell.section = 0
        elif row <= 2 and col <= 5:
            cell.section = 1
        elif row <= 2 and col <= 8:
            cell.section = 2
        elif row <= 5 and col <= 2:
            cell.section = 3
        elif row <= 5 and col <= 5:
            cell.section = 4
        elif row <=5 and col <= 8:
            cell.section = 5
        elif col <= 2:
            cell.section = 6
        elif col <= 5:
            cell.section = 7
        else:
            cell.section = 8
        cell.index = str(row) + ':' + str(col)
        self.cell_list.append(cell)
