class Solution:
    def minOperations(self, n: int) -> int:
        count = 0
        while n != 0:
            j = 1
            while j <= n:
                j = j*2
            ub = j
            lb = j/2
            n = min(abs(ub - n), abs(n - lb))
            count += 1
        return count