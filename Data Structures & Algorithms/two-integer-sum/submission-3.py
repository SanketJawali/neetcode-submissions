class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i: int = 0
        j: int = 0

        l = len(nums)
        for n in range(l):
            # Skip the last number
            if n == l - 1:
                continue
            # i is static, j loops through rest of them and find other num
            for j in range(i + 1, l):
                if nums[i] + nums[j] == target:
                    return [i, j]
            # If not found then increment
            i += 1
        print("Couldn't find")
        return [-1, -1]