from heapq import heapify_max, heappush_max, heappop_max

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        # Window pointers
        l, r = 0, (k - 1)

        heap = []
        for i in range(r):
            heappush_max(heap, (nums[i], i))

        while r < len(nums):
            # Push new element and add max to res
            # append the value and it's index
            heappush_max(heap, (nums[r], r))
            currentMax = heap[0]
            while currentMax[1] < l:
                heappop_max(heap)
                currentMax = heap[0]

            # print(heap)
            res.append(currentMax[0])

            # pop max from heap if nums[l] was max
            # if currentMax == nums[l]:
            #     heappop_max(heap)
            # else:
            #     heap.remove(nums[l])

            # 
            l += 1
            r += 1
        
        return res