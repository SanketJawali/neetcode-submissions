class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0: return 0

        # Using 2 pointers, for bubbling up the val to the end
        a, b = 0, 0

        def countk():
            k = len(nums)
            for n in nums:
                if n == val: k -= 1
            return k

        # Move a forward with each loop
        # move b to find the next element which is not == val
        while b < len(nums):
            if nums[a] == val:
                while nums[b] == val:
                    if b == len(nums) - 1:
                        break
                    b += 1
                nums[a] = nums[b]
                nums[b] = val   # Required to count k
            a += 1
            if a > b:
                b = a
        print(nums, a, b)
        return countk()