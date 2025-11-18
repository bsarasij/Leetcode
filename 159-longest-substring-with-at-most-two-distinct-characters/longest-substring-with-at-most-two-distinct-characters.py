class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        hash_map = {}
        l = r = 0
        n = len(s)
        global_max = 0
        while r < n:
            hash_map[s[r]] = hash_map.get(s[r], 0) + 1

            while len(hash_map) > 2:
                if s[l] in hash_map:
                    hash_map[s[l]] -= 1    
                if hash_map[s[l]] == 0:
                    hash_map.pop(s[l])
                l += 1
            if len(hash_map) <= 2: 
                global_max = max(global_max, r - l + 1)
            r += 1

        return global_max