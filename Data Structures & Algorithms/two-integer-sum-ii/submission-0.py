class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Using two pointers:
        # Initialize 2 pointers to start and end of the array
        # If the sum of both ints is > target
            # Find a smaller number, move R pointer <-
        # If sum of ints is < target
            # This can be possible because of -ve nums, move L ->
        
        l, r = 0, len(numbers) - 1

        while l < r:
            currsum = numbers[l] + numbers[r]
            if currsum == target:
                return [l + 1, r + 1]
            elif currsum > target:
                r -= 1
            else:
                l += 1
        