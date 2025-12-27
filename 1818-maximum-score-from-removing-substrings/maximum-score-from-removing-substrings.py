class Solution:
    def mod_string(self, s:str, target) -> str:
        s = list(s)
        stack = []
        for ch in s:
            if stack and ch == target[1] and stack[-1] == target[0]:
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)

    def maximumGain(self, s: str, x: int, y: int) -> int:
        hp = "ab" if x > y else "ba"
        lp = "ba" if x > y else "ab"
        points = 0

        #first pass
        s_p1 = self.mod_string(s, hp)
        len_diff = len(s) - len(s_p1)
        points += max(x , y) * (len_diff // 2)

        #second pass
        s_p2 = self.mod_string(s_p1, lp)
        len_diff = len(s_p1) - len(s_p2)
        points += min(x, y) * (len_diff // 2)

        return points