from collections import deque
class Solution:
    def valid(self, i, j, m, n, grid):
        return True if 0 <= i <= m - 1 and 0 <= j <= n - 1 and grid[i][j] == 1 else False
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        m, n = len(grid), len(grid[0])
        visited = [[0 for j in range(n)] for i in range(m)]
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append([i, j])
                    visited[i][j] = 1
                elif grid[i][j] == 1:
                    fresh += 1
        time = 0
        if fresh == 0:
            return 0
        # print(queue)
        while queue:
            if fresh == 0:
                return time
            l = len(queue)
            # print(fresh)
            for i in range(l):
                curr = queue.popleft()
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for di, dj in directions:
                    ni = curr[0] + di
                    nj = curr[1] + dj
                    if self.valid(ni, nj, m, n, grid) and not visited[ni][nj]:
                        visited[ni][nj] = 1
                        queue.append([ni, nj])
                        fresh -= 1

            time += 1
        return -1