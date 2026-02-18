from collections import deque
class Solution:
    def valid(self, i, j, m, n, rooms):
        return True if (0 <= i <= m - 1 and 0 <= j <= n - 1 and rooms[i][j] == 2147483647) else False

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        queue = deque()
        m, n = len(rooms), len(rooms[0])
        visited = [[0 for j in range(n)] for i in range(m)]
        dist = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append([i, j])
                    visited[i][j] = 1 
        
        while queue:
            room = queue.popleft()
            curr_i, curr_j = room[0], room[1]
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for di, dj in directions:
                n_i = curr_i + di
                n_j = curr_j + dj

                if self.valid(n_i, n_j, m, n, rooms) and (not visited[n_i][n_j]):
                    visited[n_i][n_j] = 1
                    rooms[n_i][n_j] = rooms[curr_i][curr_j] + abs(di)+ abs(dj)
                    queue.append([n_i, n_j])
