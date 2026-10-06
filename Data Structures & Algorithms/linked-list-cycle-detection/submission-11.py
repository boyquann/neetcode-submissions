# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodeSet = set()
        curr = head

        while curr not in nodeSet:
            if curr is None:
                return False
                
            nodeSet.add(curr)
            curr = curr.next



        return True


