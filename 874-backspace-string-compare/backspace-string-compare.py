class Solution:
    def reduced_str(self, s):
        s = list(s)
        stack = []
        for c in s:
            if c == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return stack
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.reduced_str(s) == self.reduced_str(t)