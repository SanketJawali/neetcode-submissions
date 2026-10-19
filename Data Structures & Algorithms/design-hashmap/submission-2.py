class node:
    def __init__(self, key: int, value: int, n: bucket = None):
        self.key = key
        self.val = value
        self.next = n

class MyHashMap:
    bucketSize = 1000
    def __init__(self):
        self.data = [None] * 1001

    def put(self, key: int, value: int) -> None:
        b = key // self.bucketSize
        cur = self.data[b]
        if not cur:
            self.data[b] = node(key, value)
        else:
            while cur.next and cur.key != key:
                cur = cur.next
            if cur.key == key:
                cur.val = value
            else:
                cur.next = node(key, value)

    def get(self, key: int) -> int:
        b = key // self.bucketSize
        cur = self.data[b]
        
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        b = key // self.bucketSize
        p = self.data[b]
        if p and p.key == key:
            self.data[b] = self.data[b].next
            return
        while p and p.next and p.next.key != key:
            p = p.next
        if p:
            p.next = p.next.next if p.next else None
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)