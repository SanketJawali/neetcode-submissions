from heapq import heapify_max, heappop_max, heappush_max, nlargest

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.heap = heapify_max(nums)
        return nlargest(k, nums)[-1]
