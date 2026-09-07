class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        res = []

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                res.extend([hashmap[diff], i])
                return res
            hashmap[n] = i