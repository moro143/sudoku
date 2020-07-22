import numpy as np

class board:

    def __init__(self, board=np.zeros([9,9], dtype=int)):
        self.board = board
        self.win = self.win_check()

    def move(self, xy, num):
        if self.board[xy[0]][xy[1]]==0:
            self.board[xy[0]][xy[1]]=num
        else:
            print("Wrong placment")

    def win_check(self):
        for n in range(9):
            for r in range(9):
                if n+1 not in self.board[r]:
                    return False
                if n+1 not in np.transpose(self.board[r]):
                    return False
            for i in range(3):
                for j in range(3):
                    if n+1 not in [self.board[3*i][3*j],self.board[3*i+1][3*j],self.board[3*i+2][3*j],self.board[3*i][3*j+1],self.board[3*i+1][3*j+1],self.board[3*i+2][3*j+1],self.board[3*i][3*j+2],self.board[3*i+1][3*j+2],self.board[3*i+2][3*j+2]]:
                        return False
        return True

    def sudoku_print(self):
        for j in range(3):
            for i in range(3):
                print(" ",self.board[i+3*j][0],self.board[i+3*j][1],self.board[i+3*j][2],"|",self.board[i+3*j][3],self.board[i+3*j][4],self.board[i+3*j][5],"|",self.board[i+3*j][6],self.board[i+3*j][7],self.board[i+3*j][8],)
            if j!=2:
                print("-------------------------")