# N-Queens
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard so that no two queens can attack each other.

# A queen in a chessboard can attack horizontally, vertically, and diagonally.

# Given an integer n, return all distinct solutions to the n-queens puzzle.

# Each solution contains a unique board layout where the queen pieces are placed. 'Q' indicates a queen and '.' indicates an empty space.

# You may return the answer in any order.

# Example 1:



# Input: n = 4

# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

from typing import List


def solveNQueens(self, n: int) -> List[List[str]]:
    res = []
    col = set()
    posDiag = set()
    negDiag = set()
    board = [["."]* n for _ in range(n)]
    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return
        for c in range(n):
            if c in col or r+c in posDiag or r-c in negDiag:
                continue
            col.add(c)
            posDiag.add(r+c)
            negDiag.add(r-c)
            board[r][c] = 'Q'
            backtrack(r+1)
            col.remove(c)
            posDiag.remove(r+c)
            negDiag.remove(r-c)
            board[r][c] = '.'
    backtrack(n)
    return res

n = 4
print(solveNQueens(n))