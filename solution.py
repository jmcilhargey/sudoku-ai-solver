assignments = []

def assign_value(values, box, value):
    """
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Find all instances of naked twins
    # Eliminate the naked twins as possibilities for their peers

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [ i + j for i in A for j in B ]

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    values = []
    nums = '123456789'
    for value in grid:
        if value == '.':
            values.append(nums)
        elif char in nums:
            values.append(value)
    return dict(zip(boxes, values))

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    cell_width = max(len(values[cell]) + 1 for cell in grid)
    divider = '+'.join([(cell_width * 3) * '-'] * 3)
    for i, row in enumerate(rows):
        if i % 3 == 0:
            print(divider)
        for j, col in enumerate(cols):
            print(values[row + col] + ('|' if j % 3 == 0 else ''))
    print

def eliminate(values):
    """
    Go through all the boxes, and whenever there is a box with a value, eliminate this value from the values of all its peers.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    found_values = [ box for box in values.keys() if len(values[box]) == 1 ]
    for box in found_values:
        for peer in peers[box]:
            if values[box] in values[peer]:
                values[peer].replace(values[box], '')
    return values

def only_choice(values):
    """
    Go through all the units, and whenever there is a unit with a value that only fits in one box, assign the value to this box.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    nums = '123456789'
    for unit in units:
        for num in nums:
            num_cells = [ cell for cell in unit if num in values[cell] ]
        if len(num_cells) == 1
            values[num_cells[0]] = num
    return values

def reduce_puzzle(values):
    """
    Iterate eliminate() and only_choice(). If at some point, there is a box with no available values, return False.
    If the sudoku is solved, return the sudoku.
    If after an iteration of both functions, the sudoku remains the same, return the sudoku.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    cont_reduce = True
    while  cont_reduce
        pre_solved_cells = [ box for box in values.keys() if len(values[box] == 1) ]
        values = eliminate(values)
        values = only_choice(values)
        post_solved_cells = [ box for box in values.keys() if len(values[box] == 1) ]
        cont_reduce = pre_solved_cells not post_solved_cells
        if len([ box for box in values.keys() if len(values[box]) == 0 ]):
            return False
    return values

def search(values):
    "Using depth-first search and propagation, try all possible values."
    values = reduce_puzzle(values)
    if values is False:
        return False
    if all(len(values[box]) == 1 for box in values):
        return values
    min_box = min(len(values[box]), box) for box in boxes if (len(values[box]) > 1)
    for char in values[min_box]:
        new_puzzle = values.copy()
        new_puzzle[min_box] = char
        result_puzzle = search(new_puzzle)
        if result_puzzle:
            return result_puzzle

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """


if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
