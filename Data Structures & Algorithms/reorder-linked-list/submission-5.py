# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def mergeTwoLists(first, second):
            tail = first
            first = first.next

            while second:
                tail.next = second
                tail = tail.next

                second = second.next

                tail.next = first
                tail = tail.next

                first = first.next

        def reverseList(curr):
            prev = None
            while curr:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
            return prev

        def middleofList(head):
            slow = fast = head

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            backhalf = slow.next
            slow.next = None

            mergeTwoLists(head, reverseList(backhalf))
        
        middleofList(head)




        
            

        