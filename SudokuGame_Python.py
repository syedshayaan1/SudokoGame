#SHAYAAN HASNAIN AHMAD
#20I-0647
#SECTION A
#AI - ASSIGNMENT 1 2.0

#Q1
#TIME AND SPACE COMPEXITY:
#TIME COMPLEXITY: O(n^(n*m)), where n is the number of possible values for each cell (i.e., 9 for Sudoku puzzles) and m is the number of empty cells in the puzzle.
#SPACE COMPLEXITY: O(1)

import heapq
import random

#THIS FUNCTION PRINTS THE PUZZLE IN A SUDOKO MANNER WITH CORRECT FORMAT

def print_puzzle(puzzle):
    for i in range(9):
        for j in range(9):
            print(str(puzzle[i][j]) + " ", end ="")
            if j == 2 or j == 5:
                print("| ", end="")
        print()
        if i == 2 or i == 5:
            print("---------------------")
    print()


#THIS FUNCTION GENERATES THE RANDOM PUZZLE ACCORDING TO THE ARG

def generate_puzzle(difficulty):
    # Create a solved puzzle
    puzzle = [[0 for j in range(9)] for i in range(9)]
    solve_puzzle(puzzle)

    # Remove cells to create the puzzle
    cells = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(cells)
    for i, j in cells:
        if random.random() <= difficulty:
            puzzle[i][j] = 0

    return puzzle

#SOLVING THE PUZZLE
#USING HEURISTIC AND A* ALGORITHMS

def solve_puzzle(puzzle):
    # Find the next empty cell with the fewest number of possible values
    row, col = find_minimal_cell(puzzle)
    if row == -1:
        # Puzzle is solved
        return True

    # Try all possible values in the cell, ordered by least to most common
    values = get_possible_values(puzzle, row, col)
    for value in values:
        puzzle[row][col] = value
        if solve_puzzle(puzzle):
            return True
        puzzle[row][col] = 0

    # Backtrack
    return False


def find_minimal_cell(puzzle):
    min_num = 10
    min_cell = (-1, -1)
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                values = get_possible_values(puzzle, i, j)
                if len(values) < min_num:
                    min_num = len(values)
                    min_cell = (i, j)
    return min_cell


def get_possible_values(puzzle, row, col):
    values = set(range(1, 10))
    values -= set(puzzle[row])
    values -= set(puzzle[i][col] for i in range(9))
    square_row = (row // 3) * 3
    square_col = (col // 3) * 3
    values -= set(puzzle[i][j] for i in range(square_row, square_row + 3) for j in range(square_col, square_col + 3))
    return sorted(list(values), key=lambda x: sum(1 for i in range(9) for j in range(9) if puzzle[i][j] == x))

def find_empty_cell(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                return i, j
    return -1, -1

def is_valid(puzzle, row, col, num):
    # Check row
    for j in range(9):
        if puzzle[row][j] == num:
            return False
    
    # Check column
    for i in range(9):
        if puzzle[i][col] == num:
            return False
    
    # Check 3x3 square
    square_row = (row // 3) * 3
    square_col = (col // 3) * 3
    for i in range(square_row, square_row + 3):
        for j in range(square_col, square_col + 3):
            if puzzle[i][j] == num:
                return False
    
    # If all checks pass, the number is valid
    return True



# EXAMPLE OF A PUZZLE 

    
puzzle = generate_puzzle(0.7)
print("RANDOM SUDUKO PUZZLE GENERATED:")
print_puzzle(puzzle)

if solve_puzzle(puzzle):
    print("SOLUTION:")
    print_puzzle(puzzle)
else:
    print("Puzzle is unsolvable.")