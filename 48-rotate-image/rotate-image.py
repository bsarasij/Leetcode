class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        left = 0
        right = n - 1
        
        while left < right:
            top, bot = left, right
            
            for i in range(right - left): 
                tmp = matrix[top][left + i]
                matrix[top][left + i] = matrix[bot - i][left]
                matrix[bot - i][left] = matrix[bot][right - i]
                matrix[bot][right - i] = matrix[top + i][right]
                matrix[top + i][right] = tmp
            left += 1
            right -= 1
        