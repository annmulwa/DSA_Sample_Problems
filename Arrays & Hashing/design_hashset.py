# Time complexity: O(n)
# Space complexity: O(n)
class MyHashSet:
    def __init__(self):
        self.data = []

    def add(self, key):
        if key not in self.data:
            self.data.append(key)

    def remove(self, key):
        if key in self.data:
            self.data.remove(key)

    def contains(self, key):
        return key in self.data

my_set = MyHashSet()
my_set.add(1)
my_set.add(2)
my_set.remove(2)
print(my_set.contains(2))
print(my_set.data)

# using a linked list to handle collisions through chaining
# Time Complexity: O(1)
# Space Complexity: O(N), where N = number of buckets
class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class HashSet:
    def __init__(self):
        self.set = [ListNode(0) for _ in range(10)]
    def add(self, key):
        cur = self.set[key % len(self.set)]

        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = ListNode(key)
    def remove(self, key):
        cur = self.set[key % len(self.set)]

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key):
        cur = self.set[key % len(self.set)]

        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False

my_set = HashSet()
my_set.add(1)
print(my_set.contains(1))
print(my_set.set)