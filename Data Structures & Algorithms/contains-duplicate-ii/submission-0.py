class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        res = False
        for j, n in enumerate(nums):
            if n in hashmap:
                i = hashmap[n]
                res = (abs(i - j) <= k) or res
            hashmap[n] = j
        return res