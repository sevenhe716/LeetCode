

# [146] https://leetcode.com/problems/lru-cache/
# Design and implement a data structure for Least Recently Used (LRU) cache.
#
# dict + double linked list
class DLinkedNode:
    def __init__(self, key, val):
        self.pre = None
        self.next = None
        self.key = key
        self.val = val


class DLinkedList:
    def __init__(self):
        self.head = DLinkedNode(0, 0)
        self.tail = DLinkedNode(0, 0)
        self.__add(self.head, self.tail)
        self.count = 0

    def remove(self, node):
        node.pre.next, node.next.pre = node.next, node.pre
        self.count -= 1

    @staticmethod
    def __add(node1, node2):
        node1.next, node2.pre = node2, node1

    def push(self, node):
        self.__add(self.tail.pre, node)
        self.__add(node, self.tail)
        self.count += 1

    def pop(self):
        first = self.head.next
        self.__add(self.head, self.head.next.next)
        self.count -= 1
        return first

    def __len__(self):
        return self.count


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = DLinkedList()
        self.dict = {}

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            self.queue.remove(node)
            self.queue.push(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            node.val = value
            self.queue.remove(node)
            self.queue.push(node)
        else:
            if len(self.queue) == self.capacity:
                del self.dict[self.queue.pop().key]
            node = DLinkedNode(key, value)
            self.dict[key] = node
            self.queue.push(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)