#!/usr/bin/python3

"""
Solving the N-queens puzzle

Checks for all the possible solutions to placing N
N non-attacking queens on an NxN chess board

Example:
    $ ./101-nqueens.py N

N HAS TO BE an integer 4 and above

Attributes:
    board (list): A list of lists representing the chess board
    solutions (list): A list of lists containing solutions

Solutions are presented in the [[r, c], [r, c], [r, c], [r, c]] format,
where 'r' is the row and 'c' represents column,
where a queen must be placed on the chess board
"""
import sys


def init_board(n):
    """
    N queens
    """

    board = []
    [board.append([]) for x in range(n)]
    [row.append(" ") for x in range(n) for row in board]
    return board


def board_deepcopy(board):
    """
    Returns a deepcopy of a chessboard
    """

    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return board


def get_solution(board):
    """
    Returns a list of lists representation of a solved chess board
    """

    solved = []
    for row in range(len(board)):
        for column in range(len(board)):
            if board[row][column] == "Q":
                solved.append([row, column])
                break
    return solved


def xout(board, row, column):
    """
    X out places on the board

    All places where non-attacking queens can no
    longer be played are X-ed out.

    Args:
        board (list): Current working chess board
        row (int): Row where a queen was last placed
        col (int): Column where a queen was last placed
    """

    # X out all forward places
    for c in range(column + 1, len(board)):
        board[row][c] = "x"

    # X out all backwards places
    for c in range(column - 1, -1, -1):
        board[row][c] = "x"

    # X out all places below
    for rw in range(row + 1, len(board)):
        board[rw][col] = "x"

    # X out all places above
    for rw in range(row - 1, -1, -1):
        board[rw][column] = "x"

    # X out all places diagonally down to the right
    c = column + 1
    for rw in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[rw][c] = "x"
        c += 1

    # X out all places diagonally up to the left
    c = col - 1
    for rw in range(row - 1, -1, -1):
        if c < 0:
            break
        board[rw][c]
        c -= 1

    # X out all places diagonally up to the right
    c = col + 1
    for rw in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[rw][c] = "x"
        c += 1

    # X out all places diagonally down to the left
    c = col - 1
    for rw in range(row + 1, len(board)):
        if c < 0:
            break
        board[rw][c] = "x"
        c -= 1


def recursive_solve(board, row, queens, solutions):
    """
    Recursively solving an N-queens puzzle

    Args:
        board (list): Current working chess board
        row (int): Current working row
        queens (int): Current number of placed queens
        resolutions (list): A list of lists of fixes

    Returns:
        resolutions
    """

    if queens == len(board):
        resolutions.append(get_solution(board))
        return resolutions

    for c in range(len(board)):
        if board[row][c] == " ":
            temp_board = board_deepcopy(board)
            temp_board[row][c] = "Q"
            xout(temp_board, row, c)
            resolutions = recursive_solve(
                temp_board, row + 1, queens + 1, resolutions)

    return resolutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    resolutions = recursive_solve(board, 0, 0, [])
    for fix in resolutions:
        print(fix)
