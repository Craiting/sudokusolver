from filehandler import FileHandler


filename = 'Puzzle-9x9-0305.txt'
# filename = 'Puzzle-16x16-0001-Inconsistant.txt'
# filename = 'Puzzle-25x25-0001-Inconsistant.txt'
# filename = 'Puzzle-9x9-0101.txt'
# filename = 'Puzzle-9x9-0203.txt'
# filename = 'Puzzle-9x9-0000-Unsolvable.txt'

puzzle = FileHandler.create_puzzle(filename)
puzzle.solve()
