class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:
    def __init__(self):
        self.map = [ListNode() for i in range(1000)]

    def hash(self, key):
        return key % len(self.map)

    def put(self, key, value):
        cur = self.map[self.hash(key)]

        while cur.next:
            if cur.next.key == key:
                cur.next.val == value
                return
            cur = cur.next
        cur.next = ListNode(key, value)

    def get(self, key):
        cur = self.map[self.hash(key)]

        while cur.next:
            if cur.next.key == key:
                return cur.next.val
            cur = cur.next
        return -1

    def remove(self, key):
        cur = self.map[self.hash(key)]

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

my_hashmap = MyHashMap()
print(my_hashmap.get(1))
my_hashmap.put(1, 2)
my_hashmap.put(2, 3)
print(my_hashmap.get(1))
print(my_hashmap.get(2))
my_hashmap.remove(2)
print(my_hashmap.get(1))
print(my_hashmap.get(2))