class Solution:
    def rob(self, nums: List[int]) -> int:
        # At each index i, we can choose the number at i + 2 or i + 3
        # We can use a bottom up dp approach
        # We calculate the optimal branches for the sums, from the bottom elements
        
        # Handle some initial cases
        if len(nums) == 1:
            return nums[0]
        
        # Append 2 dummy elements at the end
        nums.append(0)
        nums.append(0)
        
        # Consider a window of size 4
        # [0th, 1st, 2nd, 3rd]
        # We set the 0th element equal to the sum(0th, max(2nd, 3rd))
        # We set ignore the 1st element
        # We move the window left, maintaining the length of 4

        zero, two, three = len(nums) - 4, len(nums) - 2,len(nums) - 1
        for _ in range(len(nums) - 3):
            nums[zero] += max(nums[two], nums[three])
            zero -= 1
            two -= 1
            three -=1
        
        return max(nums[0], nums[1])
