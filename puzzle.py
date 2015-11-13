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
