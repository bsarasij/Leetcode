class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        up = left = 0
        down = right = n - 1
        res = [[0]*n for i in range(n)]
        idx = 0
        while idx < n**2:
            for j in range(left, right + 1):
                res[up][j] = (idx + 1)
                idx += 1
            for i in range(up + 1, down + 1):
                res[i][right] = (idx + 1)
                idx += 1
            if up < down:
                for j in range(right - 1, left - 1, -1):
                    res[down][j] = (idx + 1)
                    idx += 1
            if left < right:
                for i in range(down - 1, up, -1):
                    res[i][left] = idx + 1
                    idx += 1
            left += 1
            right -= 1
            up += 1
            down -= 1
        return res