# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodeSet = set()

        while head not in nodeSet:
            if head == None:
                return False

            nodeSet.add(head)
            head = head.next

        return True
        