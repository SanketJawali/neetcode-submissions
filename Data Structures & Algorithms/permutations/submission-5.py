class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Number of permutations: n!
        # Conditions:
        # - length of string = n, n -> len(nums)
        # - All ints in nums can be used only once in a given permutation

        # Let's choose one int from nums, we have (n - 1) choices for the next int from nums
        # For the 3rd int, we have (n - 2) choices, and so on, till only one int remains
        # i.e., n x n-1 x n-2 x n-3 x ... x 1 = n!

        # we can use a recursive approach to implement this algorithm.
        # For len(nums) = n, we can choose one of the ints from the input
        # Then we do this recursively for the list without the current chosed int
        # Say we have a sub-list of length m = n-1 we can find all combinations for that sublist.
        # When we have input of length 1, we return the only permutation, i.e., [n]

        # We are visiting n! possible permutations
        # Copying the permutation to result is O(n)
        # Overall time complexity = O(n! * n)

        # We use a used array, to keep track of elements that are used down the decision tree
        result = []
        permutation = []  # Current permutation
        used = [False] * len(nums)

        def backtrack():
            if len(permutation) == len(nums):
                result.append(permutation.copy())  # O(n)
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                permutation.append(nums[i])
                backtrack()
                used[i] = False
                permutation.pop()

        backtrack()
        return result
