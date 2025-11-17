class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count = 0
        mod_s = []
        for c in s:
            if c == '(':
                count += 1
                mod_s.append(c)
            elif c == ')' and count >  0:
                count -= 1
                mod_s.append(c)
            elif c != ')':
                mod_s.append(c)
        filtered_s = []
        for c in mod_s[::-1]:
            if c == '(' and count > 0:
                count -= 1
            else:
                filtered_s.append(c)
        return ''.join(filtered_s[::-1])