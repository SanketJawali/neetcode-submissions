class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Replace placeholders in nums1 with nums2
        for i, n in enumerate(nums2):
            nums1[m + i] = n
        
        # Sort the final list
        nums1.sort()