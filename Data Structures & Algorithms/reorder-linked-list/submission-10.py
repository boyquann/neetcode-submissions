# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def mergeTwoLists(first, second):
            dummy = ListNode()
            tail = dummy
            tail.next = first
            first = first.next

            while second:
                tail = tail.next

                tail.next = second
                second = second.next

                tail = tail.next
                tail.next = first
                first = first.next

        def reverseList(half):
            prev = None
            curr = half

            while curr:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
            return prev

        def middleofList(head):
            fast = slow = head

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            backhalf = slow.next
            slow.next = None

            mergeTwoLists(head, reverseList(backhalf))

        middleofList(head)





        
            

        