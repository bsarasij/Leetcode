class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        m = len(matrix)
        n = len(matrix[0])
        
        arr = [0 for i in range(m*n)]
        up = left = 0
        down = m - 1
        right = n - 1
        idx = 0
        while left <= right and up <= down:
            for j in range(left, right + 1):
                arr[idx] = matrix[up][j]
                idx += 1
            for i in range(up + 1, down + 1):
                arr[idx] = matrix[i][right]
                idx += 1
            if up != down:
                for j in range(right - 1, left - 1, -1):
                    arr[idx] = matrix[down][j]
                    idx += 1
            if left != right:
                for i in range(down - 1, up, -1):
                    arr[idx] = matrix[i][left]
                    idx += 1
            up += 1
            down -= 1
            left += 1
            right -= 1
        return arr