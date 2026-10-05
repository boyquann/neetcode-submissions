"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0, None, None)
        tail = dummy
        curr = head
        hashMap = {None : None}

        while curr:
            tail.next = Node(curr.val, None, None)         
            hashMap[curr] = tail.next 

            tail = tail.next
            curr = curr.next

        curr = head
        while curr:
            hashMap[curr].random = hashMap[curr.random]
            curr = curr.next

        return dummy.next



        