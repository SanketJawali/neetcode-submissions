class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0   # pointer to the index where we can place non val element

        for i in range(len(nums)):
            # With this loop, k is always pointing at position having val as value
            # In next iterations, if a non val num is found,
            # then we replace it with element at position k
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
