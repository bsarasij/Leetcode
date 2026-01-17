class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        rowSet, colSet = set(), set()


        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rowSet.add(i)
                    colSet.add(j)
        
        for i in range(m):
            for j in range(n):
                if i in rowSet or j in colSet:
                    matrix[i][j] = 0
        
                    