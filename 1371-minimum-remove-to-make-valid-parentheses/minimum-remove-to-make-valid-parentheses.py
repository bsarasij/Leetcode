class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s_list = list(s)
        stack_op = []
        count = 0
        for i, c in enumerate(s_list):
            if c == '(':
                stack_op.append(i)
                count += 1
            elif c == ')':
                if count > 0:
                    stack_op.pop()
                    count -= 1
                else:
                    s_list[i] = ""
        while stack_op:
            s_list[stack_op.pop()] = ""
        return "".join(s_list)