class Solution:
    def findMin(self, nums: List[int]) -> int:
        root = len(nums) // 2
        l, r = 0, len(nums) - 1

        # For these 3 pointers, 2 of 3 will be in same segment
        # If l < root then l and root in same segment
        # elif root < r then r and root in same segment
        # search recursively in right segment
        # first element of right segment is out answer

        print(f"{nums[l]}, {nums[root]}, {nums[r]}")
        if l == root or root == r:
            if nums[l] < nums[root]:
                return nums[l]
            else:
                return nums[root]

        if nums[root] > nums[r]:
            return self.findMin(nums[root: r + 1])
        elif nums[l] > nums[root]:
            return self.findMin(nums[l: root + 1])
        else:
            # nums is fully sorted
            return nums[l]