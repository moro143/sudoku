import numpy as np
import sudoku

def possible_by_row(y, board):
    row_having=[]
    for i in board.board[y]:
        if i!=0:
            row_having.append(i)
    row_possible=[]
    for i in range(9):
        if i+1 not in row_having:
            row_possible.append(i+1)
    return row_possible

def possible_by_column(x, board):
    column_having=[]
    for i in range(9):
        if board.board[i][x]!=0:
            column_having.append(board.board[i][x])
    column_possible=[]
    for i in range(9):
        if i+1 not in column_having:
            column_possible.append(i+1)
    return column_possible

def possible_by_cube(x, y, board):
    cube_having=[]
    cx = x//3
    cy = y//3
    for i in range(3):
        for j in range(3):
            if board.board[3*cy+i][3*cx+j]!=0:
                cube_having.append(board.board[3*cy+i][3*cx+j])
    cube_possible=[]
    for i in range(9):
        if i+1 not in cube_having:
            cube_possible.append(i+1)
    return cube_possible

def possible_all(x, y, board):
    row = possible_by_row(y, board)
    column = possible_by_column(x, board)
    cube = possible_by_cube(x, y, board)
    all_possible=[]
    for i in range(9):
        if (i+1 in row) and (i+1 in column) and (i+1 in cube):
            all_possible.append(i+1)
    return all_possible


def simple_solver(board, steps=100):
    for _ in range(steps):
        for i in range(9):
            for j in range(9):
                if board.board[i][j]==0:
                    poss = possible_all(j, i, board)
                    print(poss)
                    if len(poss)==1:
                        board.move([i,j],poss[0])
        if board.win_check():
            return True
    if not board.win_check():
        return False
    else:
        return True