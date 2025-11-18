class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l = 0
        r = 0
        n = len(s)
        max_len = 0
        ss_set = {}
        while r < n:
            ss_set[s[r]] = ss_set.get(s[r], 0) + 1
            
            while(len(ss_set) > k):
                if s[l] in ss_set:
                    ss_set[s[l]] -= 1
                if ss_set[s[l]] == 0:
                    ss_set.pop(s[l])
                l += 1
            if len(ss_set) <= k:
                max_len = max(max_len, r - l + 1)
            r += 1
        return max_len