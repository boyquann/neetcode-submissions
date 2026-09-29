# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Two trees are the same if the root are the same, have the same subtrees and each subtrees contain the same value
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if both are None
        if not p and not q:
            return True
        # if one is None and the other is not
        if not p or not q:
            return False
        # if both exist, check values
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        





