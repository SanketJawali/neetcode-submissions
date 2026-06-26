class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums) + 1)]
        result = []
        counts = {}
        for i in nums:
            if i in counts:
                counts[i] += 1
                continue
            counts[i] = 1
        print(counts)
        print(bucket)
        
        for n, freq in counts.items():
            print(n, freq)
            bucket[freq].append(n)
        
        for i in range(len(bucket) - 1, 0, -1):
            if k <= 0: break
            if len(bucket[i]) < 1: continue
            k -= len(bucket[i])
            result.extend(bucket[i])

        return result