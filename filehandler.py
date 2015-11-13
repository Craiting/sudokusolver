from puzzle4x4 import Puzzle4x4
from puzzle9x9 import Puzzle9x9
from puzzle16x16 import Puzzle16x16


class FileHandler(object):

    def __init__(self):
        self.value_mods = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,'G':16,'-':'X'}

    @staticmethod
    def create_puzzle(filename):
        self = FileHandler()
        txt = open('./SamplePuzzles/'+filename)
        raw_puzzle = txt.readlines()
        size = int(raw_puzzle[0])
        cleaned_puzzle = []
        for row in raw_puzzle[2:]:
            cleaned_puzzle.append(row.translate(None, '\n\r '))
        if size == 4:
            puzzle = Puzzle4x4()
        elif size == 9:
            puzzle = Puzzle9x9()
        elif size == 16:
            puzzle = Puzzle16x16()

        if puzzle:
            for row_num, row in enumerate(cleaned_puzzle):
                # rows = []
                for col_num, val in enumerate(row):
                    # rows.append(str(row_num) + ':' + str(col_num)+'='+val)
                    val = self.value_mods[val]
                    puzzle.create_cell(row_num, col_num, val)
                # print rows
            return puzzle
