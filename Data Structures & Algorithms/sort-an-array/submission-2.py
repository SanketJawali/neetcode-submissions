import random


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def swap(a, b):
            nums[a], nums[b] = nums[b], nums[a]

        def partition(start, end):
            # Start with random pivot
            ri = random.randint(start, end)
            swap(end, ri)

            i = start - 1
            pivot = nums[end]

            for j in range(start, end):
                if nums[j] < pivot:
                    i += 1
                    swap(i, j)

            i += 1
            swap(i, end)
            return i

        def quicksort(start, end):
            if start >= end:
                return

            pivot = partition(start, end)
            quicksort(start, pivot - 1)
            quicksort(pivot + 1, end)

        quicksort(0, len(nums) - 1)
        return nums
