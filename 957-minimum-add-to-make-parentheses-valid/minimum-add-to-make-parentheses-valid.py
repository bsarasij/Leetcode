class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        stack = []
        for c in s:
            if c == ')':
                if not stack:
                    balance += 1
                else:
                    stack.pop()
            elif c == '(':
                stack.append(c)
        return abs(balance) + len(stack)