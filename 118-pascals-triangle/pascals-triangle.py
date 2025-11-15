class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = [[0 for j in range(1, i + 1)] for i in range(1, numRows + 1)]
        for i in range(numRows):
            arr[i][0] = 1
            arr[i][-1] = 1
            if i >= 2:
                for j in range(1, len(arr[i]) - 1):
                    arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
        return arr