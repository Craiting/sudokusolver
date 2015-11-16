## Sudoku Solver
#### By Craig Tingey

To test the solver, open the main.py file and edit the filename to match the puzzle
you want to test then run 'python main.py' in the terminal. To run the tests run
python tests.py.

I used the template method to simplify the solving of different sized puzzles. The
base puzzle class has the solve method and some other methods used in the solve method
and an abstract method called create cell which creates a cell class specific to the
size of the puzzle. The create cell method is implemented in the puzzle4x4, puzzle9x9,
etc subclasses of puzzle. The algorithm is encapsulated in the solve method and it
works the same for all puzzle sizes because it follows the same methods to solve
for each size puzzle. I used the strategy pattern for the file handler. I may have used
some other patterns that I learned in class as well. 



