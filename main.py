from filehandler import FileHandler


# filename = 'Puzzle-4x4-0001.txt'
# filename = 'Puzzle-16x16-0001-Inconsistant.txt'
filename = 'Puzzle-9x9-0401.txt'
# filename = 'Puzzle-9x9-0000-Unsolvable.txt'

puzzle = FileHandler.create_puzzle(filename)
puzzle.solve()
# puzzle.debugsolve()
