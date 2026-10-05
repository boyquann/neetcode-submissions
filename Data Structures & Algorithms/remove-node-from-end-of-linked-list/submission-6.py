# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverseList(head):
            curr = head
            prev = None

            while curr:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
            return prev

        rev = reverseList(head)

        if n == 1:
            return reverseList(rev.next)

        p = rev
        q = rev

        for _ in range(n - 2):
            q = q.next
            
        p = q.next
        q.next = p.next

        return reverseList(rev)
        
        


        
        