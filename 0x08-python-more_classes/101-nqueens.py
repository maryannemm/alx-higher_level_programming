#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, col, N, solutions):
    """
    Solve N-queens problem using backtracking
    """
    if col == N:
        solution = [board[i].index(1) for i in range(N)]
        solutions.append(solution)
        return

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            solve_nqueens(board, col + 1, N, solutions)
            board[i][col] = 0

def print_solutions(N):
    """
    Print all solutions for the N-queens problem
    """
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    solve_nqueens(board, 0, N, solutions)

    for solution in solutions:
        print(solution)

def main():
    """
    Main function
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    print_solutions(N)

if __name__ == "__main__":
    main()

