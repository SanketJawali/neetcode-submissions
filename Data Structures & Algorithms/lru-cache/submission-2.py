class ListNode:
    def __init__(self, key = None, next = None, prev = None):
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.lru = None
        self.just = None

    def get(self, key: int) -> int:
        if len(self.cache) == 0:
            return -1
        # Get value
        if not key in self.cache:
            return -1
        val, old = self.cache[key]

        # Update LRU
        # 1. Create a new node
        newNode = ListNode(key=key, prev=self.just)
        # 2. Point just to new node and update pointers
        # ...old_just <=> newNode <- just
        self.just.next = newNode
        self.just = newNode
        # 3. Point old.prev <--> old.next
        # Handle old being head
        if old.prev is None:
            self.lru = old.next
            if self.lru is not None:
                self.lru.prev = None
        else:
            if old.prev is None:
                self.lru = old.next
            else:
                old.prev.next = old.next
            if old.next is not None:
                old.next.prev = old.prev
        if self.lru is None:
            self.lru = newNode
        # 4. Update cache ptr to new node
        self.cache[key] = (val, newNode)

        return val

    def put(self, key: int, value: int) -> None:
        # Update existing key
        if key in self.cache:
            old_val, old_node = self.cache[key]

            # Create new MRU node
            newNode = ListNode(key=key, prev=self.just)

            if self.just:
                self.just.next = newNode

            self.just = newNode

            # Remove old node from list
            if old_node.prev is None:
                self.lru = old_node.next
                if self.lru:
                    self.lru.prev = None
            else:
                old_node.prev.next = old_node.next
                if old_node.next:
                    old_node.next.prev = old_node.prev

            if self.lru is None:
                self.lru = newNode

            # Update cache with new value and node
            self.cache[key] = (value, newNode)
            return

        # Check capacity, add if capacity available
        # If no capcity, make it, delete lru
        if len(self.cache) == self.capacity and key not in self.cache:
            # Get LRU, remove LRU from cache and linked list
            least = self.lru.key
            self.cache.pop(least)
            self.lru = self.lru.next

            if self.lru is not None:
                self.lru.prev = None

        # Create new List node, add key-value to cache
        newNode = ListNode(key=key, prev=self.just)
        self.cache[key] = (value, newNode)
        # Update just used ptr
        if self.just:
            self.just.next = newNode
        self.just = newNode
        if self.lru is None:
            self.lru = newNode

    def appendNewNode(self, node):
        pass