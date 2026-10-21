from heapq import heappush, heappop

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.data = []
        self.k = k
        for n in nums:
            if len(self.data) == k and n > self.data[0]:
                heappop(self.data)
                heappush(self.data, n)
            elif len(self.data) < k:
                heappush(self.data, n)

    def add(self, val: int) -> int:
        if len(self.data) == self.k:
            if val > self.data[0]:
                heappop(self.data)
                heappush(self.data, val)
        else:
            heappush(self.data, val)
        return self.data[0]
