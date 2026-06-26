from heapq import heapify_max, heappush_max, nlargest
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k

        heapify_max(self.heap)
        self.nlarge = None

    def add(self, val: int) -> int:
        heappush_max(self.heap, val)
        print(self.heap)
        if len(self.heap) > self.k:
            self.nlarge = nlargest(self.k, self.heap)
        elif len(self.heap) > 0:
            self.nlarge = nlargest(len(self.heap), self.heap)
        print(self.nlarge)
        return self.nlarge[-1]