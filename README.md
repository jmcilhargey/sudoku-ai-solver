# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: Sometimes we come across a pair of squares in a row, column, or 3 x 3 unit that can be 1 of 2 values. We know the values go into those two boxes, although we can't say which value goes in which box. However, our algorithm can use this information as a constraint to eliminate those 2 values from all other boxes in the row, column, or 3 x 3 unit where the pair appears. The naked twin introduces a constraint in the number of possible values. We exploit this limitation to reduce the number of possible values for related boxes.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: A diagonal suduko specifies that 1 - 9 must appear once along the 2 main diagonals of the puzzle. This introduces an additional constraint since for any value we choose in the puzzle, we must verify it doesn't violate this rule. We use this to our advantage in the algorithm since we may evaluate squares where a diagonal constraint allows us to reduce the number of possible values for a box. Enforcing this rule allows us to assign values with greater efficiency.

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project.
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.
