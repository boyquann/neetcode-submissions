# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Each node need to figure out instantly if they are the LCA otherwise, move to the subtree (either right or left) that signals where p and q are and repeat

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right

            elif p.val < root.val and q.val < root.val:
                root = root.left
            
            else:
                return root

            
    

        


