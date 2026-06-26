class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = {}
        starts = {}
        if len(nums) < 1:   # If no element in list
            return 0
        if len(nums) == 1:  # if only 1 element in list
            return 1

        for n in nums:
            if n not in hashmap:
                hashmap[n] = n

        if len(hashmap) == 1:  # only 1 unique element
            return 1
        
        for n in nums:
            if n - 1 not in hashmap:
                starts[n] = 0
            
        for seq in starts.keys():
            starts[seq] = self.getSeqLen(seq, hashmap)
        
        return max(list(starts.values()))
            
    def getSeqLen(self, current, hashmap) -> int:
        if current + 1 in hashmap:
            return self.getSeqLen(current + 1, hashmap) + 1
        else:
            return 1