import random


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counts = {i: 0 for i in range(3)}

        for c in nums:
            counts[c] += 1
        
        ptr = 0
        for c in range(3):
            for n in range(counts[c]):
                nums[ptr + n] = c
            ptr += counts[c]