class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if k == 0: return   # No rotation

        def reverse(start, end):
            l, r = start, end
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        n = len(nums)
        k = k % n   # if k > n, we only need k % n rotations
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)