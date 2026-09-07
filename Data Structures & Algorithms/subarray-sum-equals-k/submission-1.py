class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # MISTAKE:
        # Sliding Window: Doesn't work because the array contains negative numbers.
        
        res = 0
        currsum = 0

        # Don't calculate prefix sum beforehand
        prefix = {0: 1} # Initialize value of 0, indicating null subarray

        for n in nums:
            currsum += n
            diff = currsum - k

            res += prefix.get(diff, 0)
            prefix[currsum] = 1 + prefix.get(currsum, 0)
        
        return res