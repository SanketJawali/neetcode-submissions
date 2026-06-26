from heapq import heapify_max, heappush_max, heappop_max

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        # Window pointers
        l, r = 0, (k - 1)

        heap = nums[l:r]
        heapify_max(heap)

        while r < len(nums):
            # Push new element and add max to res
            heappush_max(heap, nums[r])
            currentMax = heap[0]
            # print(heap)
            res.append(currentMax)

            # pop max from heap if nums[l] was max
            if currentMax == nums[l]:
                heappop_max(heap)
            else:
                heap.remove(nums[l])
            l += 1
            r += 1
        
        return res