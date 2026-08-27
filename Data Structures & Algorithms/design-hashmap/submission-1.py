class Node:
    def __init__(self, key, value = None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        # A list of size 1000
        # Each cell in the list contains a pointer to a Linked list
        self.data = [None] * 1000

    def put(self, key: int, value: int) -> None:
        h = self.hash(key)
        if self.data[h] is None:
            self.data[h] = Node(key, value)

        ptr = self.data[h]    # Pointer to current node
        while ptr:
            if ptr.key == key:
                ptr.value = value
                break
            elif ptr.next:
                ptr = ptr.next
            else:
                ptr.next = Node(key, value)

    def get(self, key: int) -> int:
        h = self.hash(key)
        ptr = self.data[h]

        while ptr:
            print(ptr.key, key)
            if ptr.key == key: return ptr.value
            ptr = ptr.next
        return -1

    def remove(self, key: int) -> None:
        h = self.hash(key)
        prev = None
        ptr = self.data[h]

        while ptr:
            if prev is None and ptr.key == key:
                self.data[h] = ptr.next
                break
            if ptr.key == key:
                prev.next = ptr.next
                break
            prev = ptr
            ptr = ptr.next
        
    def hash(self, key: int) -> int:
        return key % 1000

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)