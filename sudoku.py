# Title: Sudoku
# Difficulty level: HARD
# Link: https://www.geeksforgeeks.org/sudoku-backtracking-7/

# Given a partially filled 9×9 2D array ‘grid[9][9]’, the goal is to assign digits (from 1 to 9) to the empty cells
# so that every row, column, and subgrid of size 3×3 contains exactly one instance of the digits from 1 to 9.

# Example:
# Input:
# grid = { {3, 0, 6, 5, 0, 8, 4, 0, 0},
#          {5, 2, 0, 0, 0, 0, 0, 0, 0},
#          {0, 8, 7, 0, 0, 0, 0, 3, 1},
#          {0, 0, 3, 0, 1, 0, 0, 8, 0},
#          {9, 0, 0, 8, 6, 3, 0, 0, 5},
#          {0, 5, 0, 0, 9, 0, 6, 0, 0},
#          {1, 3, 0, 0, 0, 0, 2, 5, 0},
#          {0, 0, 0, 0, 0, 0, 0, 7, 4},
#          {0, 0, 5, 2, 0, 6, 3, 0, 0} }
# Output:
# 3 1 6 5 7 8 4 9 2
# 5 2 9 1 3 4 7 6 8
# 4 8 7 6 2 9 5 3 1
# 2 6 3 4 1 5 9 8 7
# 9 7 4 8 6 3 1 2 5
# 8 5 1 7 9 2 6 4 3
# 1 3 8 9 4 7 2 5 6
# 6 9 2 3 5 1 8 7 4
# 7 4 5 2 8 6 3 1 9
# Explanation: Each row, column and 3*3 box of
# the output matrix contains unique numbers.

### Transposes a matrix
def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


### Checks if the board has no empty boxes
def is_board_completed(board):
    zero_cells_count = 0
    for row in board:
        for element in row:
            if element == 0:
                zero_cells_count += 1
    return zero_cells_count == 0


def get_board_subgrid(board, row, col):
    assert 0 <= row < 9
    assert 0 <= col < 9

    row_start = row - row % 3
    row_end = row_start + 2

    col_start = col - col % 3
    col_end = col_start + 2
    return board[row_start:row_end][col_start:col_end]


### Checks standard sudoku rules for new move
def is_element_valid_in_position(board, row, col, new_el):
    # Check position and el to be valid
    if new_el == 0:
        return False
    if row < 0 or row >= 9:
        return False
    if col < 0 or col >= 9:
        return False

    if board[row][col] != 0:
        return False
    # Check row
    for el in board[row]:
        if el == new_el:
            return False
    # Check column
    for el in transpose(board)[col]:
        if el == new_el:
            return False
    # Check subgrid
    subgrid = get_board_subgrid(board, row, col)
    for row in subgrid:
        for el in row:
            if el == new_el:
                return False

    return True

def solve(board):
    return solve(board, 0, 0)

def solve(board, row, col):
    if is_board_completed(board):
        return True


    for new_move in range(9):
