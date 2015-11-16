import unittest
from filehandler import FileHandler
from puzzle import Puzzle

class TestFileHandler(unittest.TestCase):

    def test_load_4x4_puzzle(self):
        filename = 'Puzzle-4x4-0001.txt'
        puzzle = FileHandler.create_puzzle(filename)
        self.assertEqual(4,puzzle.size)

    def test_load_9x9_puzzle(self):
        filename = 'Puzzle-9x9-0001.txt'
        puzzle = FileHandler.create_puzzle(filename)
        self.assertEqual(9,puzzle.size)

    def test_load_16x16_puzzle(self):
        filename = 'Puzzle-16x16-0001-Inconsistant.txt'
        puzzle = FileHandler.create_puzzle(filename)
        self.assertEqual(16,puzzle.size)

class TestPuzzle(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        filename4 = 'Puzzle-4x4-0001.txt'
        filename9 = 'Puzzle-9x9-0001.txt'
        filename16 = 'Puzzle-16x16-0001-Inconsistant.txt'
        self.puzzle4x4 = FileHandler.create_puzzle(filename4)
        self.puzzle9x9 = FileHandler.create_puzzle(filename9)
        self.puzzle16x16 = FileHandler.create_puzzle(filename16)
        self.assertEqual(4, self.puzzle4x4.size)
        self.assertEqual(9, self.puzzle9x9.size)
        self.assertEqual(16, self.puzzle16x16.size)


    def test_get_same_row(self):
        self.assertEqual([4,9,1,3,6,7,8], self.puzzle9x9.get_same_row(0))
        self.assertEqual([1,6,4,8], self.puzzle9x9.get_same_row(5))
        self.assertEqual([3,9,4,8,7], self.puzzle9x9.get_same_row(8))

    def test_get_same_col(self):
        self.assertEqual([4,5,1,3], self.puzzle9x9.get_same_col(0))
        self.assertEqual([3,2,1,6,5,8], self.puzzle9x9.get_same_col(4))
        self.assertEqual([8,4,5], self.puzzle9x9.get_same_col(8))

    def test_get_same_section(self):
        self.assertEqual([4,9,6,3,5], self.puzzle9x9.get_same_section(0))
        self.assertEqual([3,1,6,4], self.puzzle9x9.get_same_section(4))
        self.assertEqual([2,5,8,3,7], self.puzzle9x9.get_same_section(8))

    def test_create_cell(self):
        cell4x4 = self.puzzle4x4.create_cell(1,3,'-')
        self.assertEqual(1,cell4x4.row)
        self.assertEqual(3,cell4x4.col)
        self.assertEqual(2,cell4x4.section)
        self.assertEqual([1,2,3,4],cell4x4.possible_values)
        # cell4x4_value = self.puzzle4x4.create_cell(0,0,5)






if __name__ == '__main__':
    unittest.main()
