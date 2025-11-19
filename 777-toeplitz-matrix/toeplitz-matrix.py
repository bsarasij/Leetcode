class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                if i > 0 and j > 0:
                    if matrix[i][j] != matrix[i - 1][j - 1]:
                        return False
        return True