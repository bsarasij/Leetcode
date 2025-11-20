class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        n = len(num)
        curr_max = num[-1]
        max_idx = n-1
        max_right = [None for i in range(n)]
        for i in reversed(range(len(num))):
            if num[i] > curr_max:
                curr_max = num[i]
                max_idx = i
            
            max_right[i] = max_idx
            
        for i in range(n):
            if num[max_right[i]] > num[i]:
                num[max_right[i]], num[i] = num[i], num[max_right[i]]
                break

        return int("".join(num))
