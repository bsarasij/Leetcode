from collections import Counter
class Solution:
    def compress(self, chars: List[str]) -> int:
        insertidx = 0
        r = 0
        n = len(chars)
        while r < n:
            group = 1
            while (r + group) < n and chars[r + group] == chars[r]:
                group += 1
            chars[insertidx] = chars[r]
            insertidx += 1
            if group > 1:
                chars[insertidx : insertidx + len(str(group))] = list(str(group))
                insertidx += len(str(group))
            r += group
        return insertidx