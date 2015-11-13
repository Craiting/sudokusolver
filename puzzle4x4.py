from puzzle import Puzzle
from cell import Cell


class Puzzle4x4(Puzzle):

    def __init__(self):
        super(Puzzle4x4, self).__init__()
        self.size = 4

    def create_cell(self, row, col, value):
        possible_values = [1,2,3,4]
        if value != '-':
            possible_values = 'none'
        cell = Cell(row, col, value, possible_values)
        if row <= 1 and col <= 1:
            cell.section = 0
        elif row <= 1:
            cell.section = 1
        elif col <= 1:
            cell.section = 2
        else:
            cell.section = 3
        cell.index = str(row) + ':' + str(col)
        self.cell_list.append(cell)
