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

    def eliminate_by_possibilities(self):
        for cell in self.cell_list:
            if cell.value == '-':
                if(self.compare_possibilities(cell) != False):
                    cell.value = self.compare_possibilities(cell)
                    print 'found', cell.value, cell.index
                    cell.possible_values = [cell.value]
                    break

    def compare_possibilities(self, thecell): # this checks the possible values of all cells in the same index, it can maybe narrow down an answer
        if thecell.possible_values != 'none':
            vals = self.compare_within_section(thecell)
            if(len(vals) ==1):
                # thecell.value = vals[0]
                thecell.possible_values = vals
            vals = self.compare_within_row(thecell)
            if(len(vals) ==1):
                # thecell.value = vals[0]
                thecell.possible_values = vals
            vals = self.compare_within_col(thecell)
            if(len(vals) ==1):
                # thecell.value = vals[0]
                thecell.possible_values = vals
        return False

    def compare_within_section(self, thecell):
        check = thecell.possible_values
        for cell in self.cell_list:
            if cell.index != thecell.index and cell.possible_values != 'none':
                if cell.section == thecell.section:
                    if type(cell.value) == str:
                        check = [item for item in check if item not in cell.possible_values]
                        if len(check) == 0:
                            break
        if len(check) == 1:
            return check
        else:
            return thecell.possible_values

    def compare_within_row(self, thecell):
        check = thecell.possible_values
        for cell in self.cell_list:
            if cell.index != thecell.index and cell.possible_values != 'none':
                if cell.row == thecell.row:
                    if type(cell.value) == str:
                        check = [item for item in check if item not in cell.possible_values]
                        if len(check) == 0:
                            break
        if len(check) == 1:
            return check
        else:
            return thecell.possible_values

    def compare_within_col(self, thecell):
        check = thecell.possible_values
        for cell in self.cell_list:
            if cell.index != thecell.index and cell.possible_values != 'none':
                if cell.col == thecell.col:
                    if type(cell.value) == str:
                        check = [item for item in check if item not in cell.possible_values]
                        if len(check) == 0:
                            break
        if len(check) == 1:
            return check
        else:
            return thecell.possible_values


    def get_solved(self):
        solved = True
        for cell in self.cell_list:
            if cell.value == '-':
                solved = False
        return solved

    def solve(self):
        temp_count = 0
        while (not self.get_solved()):
            self.eliminate_by_surroundings()
            self.eliminate_by_possibilities()
            temp_count+=1
            if temp_count >= 500:
                break
        print 'solvable = ' + str(self.get_solved())
        self.show()
        if self.get_solved():
            self.output_to_file()

    def eliminate_by_surroundings(self):
        temp_count = 0
        while (not self.get_solved()):
            for cell in self.cell_list:
                if cell.value == '-':
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
                        break
            temp_count += 1
            if temp_count == self.size*self.size:
                break

    def get_cell_by_index(self,row,col):
        for cell in self.cell_list:
            ind = str(row) + ':' + str(col)
            if ind == cell.index:
                return cell

    def show(self):
        for i in range(0,self.size):
            line = []
            for j in range(0, self.size):
                line.append(str(self.get_cell_by_index(i,j).value))
            print line

    def output_to_file(self):
        filename = 'output.txt'
        f = open(filename, 'w')
        for i in range(0,self.size):
            f.write(str(self.get_same_row(i))+'\n')
