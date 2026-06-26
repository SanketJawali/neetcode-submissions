class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Iterate through the nums list, and count all the nums
        # create a hashmap for all the unique nums, and counts as the values
        # return k nums with highest counts

        counts = {}

        for i in nums:
            if i in counts:
                # Increment the count for the num
                counts[i] += 1
            else:
                counts[i] = 1
            
        # list to return
        results = []

        inv_counts = {}

        for kc, vc in counts.items():
            if vc in inv_counts:
                inv_counts[vc] += [kc]
            else:
                inv_counts[vc] = [kc]
        
        highest_counts = list(inv_counts.keys())
        highest_counts.sort(reverse=True)

        while len(results) < k:
            if len(highest_counts) > 0:
                nums = inv_counts[highest_counts[0]]
                results.extend(list(nums))
                highest_counts.pop(0)
                print(results)


        if len(results) == k:
            return results
        else:
            return []
