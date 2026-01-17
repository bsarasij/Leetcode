class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        rowArr, colArr = [False for i in range(m)], [False for j in range(n)]


        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rowArr[i] = True
                    colArr[j] = True
        
        for i in range(m):
            for j in range(n):
                if rowArr[i] or colArr[j]:
                    matrix[i][j] = 0
        
                    