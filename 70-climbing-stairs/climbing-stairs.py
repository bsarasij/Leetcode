class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1;
        f_i = 0
        f_ip1 = 1
        i = 0
        for i in range(n):
            f_i, f_ip1 = f_ip1, f_i + f_ip1
        return f_ip1