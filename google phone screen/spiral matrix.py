# Spiral Matrix
# Given an m x n matrix, return all elements of the matrix in spiral order.
# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:


# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100

from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1
        output = []
        while len(output) < len(matrix) * len(matrix[0]):
            for i in range(left,right+1):
                output.append(matrix[top][i])
            top += 1
            for i in range(top,bottom+1):
                output.append(matrix[i][right])
            right -= 1
            if len(output) >= len(matrix) * len(matrix[0]):
                break
            for i in range(right,left-1,-1):
                output.append(matrix[bottom][i])
            bottom -= 1
            for i in range(bottom,top-1,-1):
                output.append(matrix[i][left])
            left += 1
        return output