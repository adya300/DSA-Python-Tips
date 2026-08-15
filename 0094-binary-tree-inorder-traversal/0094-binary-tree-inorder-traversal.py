# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        r=[]
        def dfs(n):
            if n==None:
                return
            dfs(n.left)
            r.append(n.val)
            dfs(n.right)
        dfs(root)
        return r