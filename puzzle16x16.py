from puzzle import Puzzle
from cell import Cell


class Puzzle16x16(Puzzle):

    def create_cell(self, row, col, value):
        possible_values = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        cell = Cell(row, col, value, possible_values)
        if row <= 3 and col <= 3:
            cell.section = 0
        elif row <= 3 and col <= 7:
            cell.section = 1
        elif row <= 3 and col <= 11:
            cell.section = 2
        elif row <= 3 and col <= 15:
            cell.section = 3
        elif row <= 7 and col <= 3:
            cell.section = 4
        elif row <= 7 and col <= 7:
            cell.section = 5
        elif row <= 7 and col <= 11:
            cell.section = 6
        elif row <= 7 and col <= 15:
            cell.section = 7
        elif row <= 11 and col <= 3:
            cell.section = 8
        elif row <= 11 and col <= 7:
            cell.section = 9
        elif row <= 11 and col <= 11:
            cell.section = 10
        elif row <= 11 and col <= 15:
            cell.section = 11
        elif col <= 3:
            cell.section = 12
        elif col <= 7:
            cell.section = 13
        elif col <= 11:
            cell.section = 14
        else:
            cell.section = 15
        cell.index = str(row) + ':' + str(col)
        self.cell_list.append(cell)
