class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        ans = [[None for j in range(m)] for i in range(n)]        
        for r in range(m):
            for c in range(n):
                ans[c][r] = matrix[r][c]
        return ans