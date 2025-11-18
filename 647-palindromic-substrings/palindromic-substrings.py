class Solution:
    def palin(self, s, l, r, n):
        count = 0
        while l >= 0 and r < n and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        return count


    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        for i in range(n):
            count += self.palin(s, i, i, n)
            count += self.palin(s, i, i + 1, n)
        return count