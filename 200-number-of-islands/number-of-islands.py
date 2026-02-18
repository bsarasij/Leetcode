class Solution:
    def valid(self, i, j, m, n):
        return True if 0 <= i <= m - 1 and 0 <= j <= n - 1 else False
        
    def dfs(self, i, j, m, n, grid, visited):
        visited[i][j] = 1
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if self.valid(ni, nj, m, n) and grid[i][j] == "1" and not visited[ni][nj]:
                self.dfs(ni, nj, m, n, grid, visited)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        islands = 0
        visited = [[0 for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == "1":
                    islands += 1
                    self.dfs(i, j, m, n, grid, visited)
        return islands