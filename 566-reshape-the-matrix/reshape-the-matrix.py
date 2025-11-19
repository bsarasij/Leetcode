class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m*n != r*c or m == 0 or n == 0:
            return mat
        res = [[0 for j in range(c)] for i in range(r)]
        k, l = 0, 0
        for i in range(m):
            for j in range(n):
                res[k][l] = mat[i][j]
                l += 1
                if l == c:
                    k += 1
                    l = 0
        return res