class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        arr = [0 for i in range(m*n)]
        i = 0
        up = True
        row = col = 0
        while row < m and col < n:
            if up:
                while (row > 0 and col < n - 1):
                    arr[i] = mat[row][col]
                    row -= 1
                    col += 1
                    i += 1
                arr[i] = mat[row][col]
                i += 1
                if col == n-1:
                    row += 1
                else:
                    col += 1
            else:
                while (col > 0 and row < m - 1):
                    arr[i] = mat[row][col]
                    row += 1
                    col -= 1
                    i += 1
                arr[i] = mat[row][col]
                i += 1
                if row == m - 1:
                    col += 1
                else:
                    row += 1
            up = not up
        return arr