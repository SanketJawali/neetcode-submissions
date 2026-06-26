class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 1, len(numbers)

        for _ in range(len(numbers)):
            total = numbers[l - 1] + numbers[r - 1]
            # print(l, r, total)
            if total == target:
                return [l, r]
            elif total < target:
                l += 1
            else:
                # total > target
                r -= 1
        
        return [-1, -1]