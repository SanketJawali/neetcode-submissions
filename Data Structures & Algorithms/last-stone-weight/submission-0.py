from heapq import heapify_max, heappush_max, heappop_max
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapify_max(stones)

        while len(stones) > 1:
            a = heappop_max(stones)
            b = heappop_max(stones)

            remain = a - b
            if remain > 0:
                heappush_max(stones, remain)
            
        if len(stones) == 1:
            return stones[0]
        return 0