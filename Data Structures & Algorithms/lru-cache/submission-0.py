class ListNode():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        save = self.right.prev
        self.right.prev = node
        node.next = self.right
        node.prev = save
        save.next = node
        
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)

            return node.val

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)

        else:
            node = ListNode(key, value)
            self.cache[key] = node
            self.insert(node)

        if len(self.cache) > self.capacity:
            node = self.left.next
            self.remove(node)
            del self.cache[node.key]
        