class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row, col = len(matrix), len(matrix[0])
        left = 0
        up = 0
        right = col - 1
        down = row - 1
        results = []
        while len(results) < row*col:
            for j in range(left, right + 1):
                results.append(matrix[up][j])
            for i in range(up + 1, down + 1):
                results.append(matrix[i][right])
            if up != down: 
                for j in range(right - 1, left - 1, -1):
                    results.append(matrix[down][j])
            if right != left:
                for i in range(down - 1, up, -1):
                    results.append(matrix[i][left])
            up += 1
            left += 1
            right -= 1
            down -= 1
        return results