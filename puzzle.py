import abc

class Puzzle(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.size = None
        self.cell_list = []

    @abc.abstractmethod
    def create_cell(self):
        """Creates a cell specific to puzzle size"""

    def get_same_row(self, row): # takes an integer for the row
        values = []
        for cell in self.cell_list:
            if cell.row == row and type(cell.value) == int:
                values.append(cell.value)
        return values

    def get_same_col(self, col): # takes an integer for the col
        values = []
        for cell in self.cell_list:
            if cell.col == col and type(cell.value) == int:
                values.append(cell.value)
        return values

    def get_same_section(self, section):
        values = []
        for cell in self.cell_list:
            if cell.section == section and type(cell.value) == int:
                values.append(cell.value)
        return values

    def get_solved(self):
        solved = True
        for cell in self.cell_list:
            if cell.value == 'X':
                solved = False
        return solved

    def solve(self):
        while (not self.get_solved()):
            for cell in self.cell_list:
                if cell.value == 'X':
                    samerow = self.get_same_row(cell.row)
                    for val in samerow:
                        try:
                            cell.possible_values.remove(val)
                        except:
                            pass
                    samecol = self.get_same_col(cell.col)
                    for val in samecol:
                        try:
                            cell.possible_values.remove(val)
                        except:
                            pass
                    samesection = self.get_same_section(cell.section)
                    for val in samesection:
                        try:
                            cell.possible_values.remove(val)
                        except:
                            pass
                    if len(cell.possible_values) == 1:
                        cell.value = cell.possible_values[0]
        print 'solved'
        self.show()

    def show(self):
        for i in range(0,self.size):
            print self.get_same_row(i)
