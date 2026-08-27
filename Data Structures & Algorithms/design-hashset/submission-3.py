class MyHashSet:

    def __init__(self):
        self.data = [0] * 1_000_001

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.data[key] = 1

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.data[key] = 0

    def contains(self, key: int) -> bool:
        return self.data[key] == 1


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)