class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        # print(path)
        stack = []
        for idx, item in enumerate(path):
            if item == '..':
                if stack:
                    stack.pop()
            elif item == '.' or not item:
                continue
            else:
                stack.append(item)
        return "/" + "/".join(stack)