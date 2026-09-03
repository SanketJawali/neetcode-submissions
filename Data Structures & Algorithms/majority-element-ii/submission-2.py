class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        limit = len(nums) // 3
        counts = defaultdict(int)

        for n in nums:
            counts[n] += 1

            if len(counts) <= 2: continue
            
            new_count = defaultdict(int)
            for k, v in counts.items():
                if v > 1:
                    new_count[k] = v - 1
            counts = new_count

        res = list()
        for n in counts:
            if nums.count(n) > limit:
                res.append(n)
        return res