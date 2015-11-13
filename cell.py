

class Cell(object):

    def __init__(self, row, col, value, possible_vals):
        self.row = row
        self.col = col
        self.value = value
        self.possible_values = possible_vals
        self.section = None
        self.index = None
