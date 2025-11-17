class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        hash_map = {}
        l = r = 0
        n = len(s)
        max_len = - inf
        while r < n:
            if s[r] in hash_map:
                if hash_map[s[r]] >= l:
                    l = hash_map[s[r]] + 1
            length = r - l + 1
            max_len = max(max_len, length)
            hash_map[s[r]] = r
            r += 1
        return max_len