class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for n in nums:
            # For n, mark nums[n - 1] as -1
            # if ever we see a -1 as value of nums[n - 1]
            # the element is already encountered
            n = -n if n < 0 else n

            print("n: ", n, ", nums[n]: ", nums[n])
            if nums[n - 1] < 0:
                return n
            else:
                nums[n - 1] = -nums[n - 1]
