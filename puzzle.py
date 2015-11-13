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

    def compare_possiblities(self, thecell): # this checks the possible values of all cells in the same index, it can maybe narrow down an answer
        for c in thecell.possible_values:
            answer = c
            for cell in self.cell_list:
                if cell.section == thecell.section and type(cell.value) == int:
                    if c in cell.possible_values:
                        answer = False
        if answer:
            return answer

    def get_solved(self):
        solved = True
        for cell in self.cell_list:
            if cell.value == '-':
                solved = False
        return solved

    def solve(self):
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
                    if(self.compare_possiblities(cell) not False):
                        cell.value = self.compare_possiblities(cell)
                        cell.possible_values = [cell.value]
            temp_count += 1
            if temp_count == 5000:
                # print '##################'
                # for cell in self.cell_list:
                #     print cell.possible_values
                # print '##################'
                break
        # print 'solvable = ' + str(self.get_solved())
        # self.show()
        if self.get_solved():
            self.output_to_file()


    def debugsolve(self):
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
        self.show()

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
