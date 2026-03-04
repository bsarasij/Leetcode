# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, node):
        if node is None:
            return -1 
        if (node.left is None and node.right is None):
            return 0
        contribution = 1 + max(self.height(node.left), self.height(node.right))
        return contribution 
 
    def dfs(self, node, maxDia):
        if not node:
            return -1
        left_height = -1
        right_height = -1
        if node.left:
            left_height = self.height(node.left)
        if node.right:
            right_height = self.height(node.right)
        maxDia[0] = max(maxDia[0], 2 + left_height + right_height)
        self.dfs(node.left, maxDia)
        self.dfs(node.right, maxDia)

        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxDia = [0]
        self.dfs(root, maxDia)
        return maxDia[0]