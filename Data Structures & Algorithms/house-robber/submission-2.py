class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = rob2 = 0

        # [rob1, rob2, n, n+1, n+2...]
        # [x, rob1, rob2, n, n+1...]
        # Check max(rob1 + n, rob2) 
        # We can rob current house and house two steps before, or not rob current house
        # If we choose not to rob, the max money we have is same as past one

        for n in nums:
            maxRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = maxRob
        
        return rob2