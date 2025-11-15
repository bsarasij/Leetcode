class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m = len(a) - 1
        n = len(b) - 1
        res = []
        carry = 0
        while m >= 0 or n >= 0 or carry > 0:
            x, y = int(a[m]) if m >= 0 else 0, int(b[n]) if n >= 0 else 0
            tot = x + y + carry
            bit = tot % 2
            carry = tot // 2
            res.append(str(bit))
            m-= 1
            n -= 1
        return ''.join(reversed(res))