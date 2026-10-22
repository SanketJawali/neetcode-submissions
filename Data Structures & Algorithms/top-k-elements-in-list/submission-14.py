from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # List of sets, index -> freq.
        buckets = []
        for _ in range(len(nums)):
            buckets.append(set())

        # Frequency of each unique element
        counts = defaultdict(int)

        # Count elements
        for n in nums:
            counts[n] += 1
            c = counts[n]
            buckets[c - 1].add(n)   # -1 for zero indexing
        
        # Find most freq elements
        res = set()

        while len(res) < k:
            while len(buckets[-1]) == 0:
                buckets.pop()
            res.add(buckets[-1].pop())
            if len(buckets[-1]) == 0:
                buckets.pop()
        
        return list(res)
