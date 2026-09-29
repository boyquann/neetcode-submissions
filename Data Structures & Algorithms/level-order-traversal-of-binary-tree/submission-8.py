# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            level = []
            while queue:
                node = queue.popleft()
                level.append(node)

            result.append([x.val for x in level])

            for node in level:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result
