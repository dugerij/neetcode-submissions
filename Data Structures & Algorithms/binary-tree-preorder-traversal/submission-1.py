# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # stack = [root]
        # res = []

        # while stack:
        #     current = stack.pop()
        #     if current:
        #         stack.append(current.right)
        #         stack.append(current.left)
        #         res.append(current.val)
        
        # return res
        res = []

        def dfs(root):
            if root:
                res.append(root.val)
                dfs(root.left)
                dfs(root.right)
        dfs(root)

        return res
