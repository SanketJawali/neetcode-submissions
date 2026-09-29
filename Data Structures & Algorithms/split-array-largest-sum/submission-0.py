class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        res = r

        def split(largest):
            subarray = 0
            cursum = 0
            for n in nums:
                cursum += n
                if cursum > largest:
                    subarray += 1
                    cursum = n
            return subarray + 1 <= k

        while l <= r:
            mid = l + ((r - l) // 2)
            canSplit = split(mid)
            if canSplit:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res
