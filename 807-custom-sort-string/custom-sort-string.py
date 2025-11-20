from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        a = Counter(s)
        res = []
        for c in order:
            if c in order:
                res.append(c*a[c])
                del a[c]
        for key in a:
            res.append(key*a[key])
            
        return "".join(res)