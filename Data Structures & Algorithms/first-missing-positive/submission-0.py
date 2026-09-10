class Solution:
    def firstMissingPositive(self, n: List[int]) -> int:
        # Remove all negative numbers from the input, because they don't matter
        for i in range(len(n)):
            if n[i] < 0:
                n[i] = 0
        
        # For all number which are in-bounds, mark the corresponding index with -ve
        # Bounds: 1 <= x <= len(n); because smallest -ve can be len(n) + 1 in worst case
        for i in range(len(n)):
            val = abs(n[i])

            if 1 <= val <= len(n):
                if n[val - 1] > 0:
                    n[val - 1] *= -1
                elif n[val - 1] == 0:
                    n[val - 1] = -1 * (len(n) + 1)
        
        # Find smallest number within bounds, and have index not marked -ve
        for i in range(1, len(n) + 1):
            if n[i - 1] >= 0:
                return i
        
        return len(n) + 1
