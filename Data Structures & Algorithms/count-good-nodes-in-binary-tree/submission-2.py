# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# if you are None, return 0 otherwise compare yourself with nthe current pathMax, if you are greater than or equal to that, increment a counter, otherwise ask your children the same thing

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.count = 0

        def dfs(root, pathMax):
            if not root:
                return 0

            if root.val >= pathMax:
                self.count += 1
                pathMax = root.val

            dfs(root.left, pathMax)
            dfs(root.right, pathMax)

        dfs(root, root.val)
        return self.count

        
        