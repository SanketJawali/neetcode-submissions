class Solution:
    def climbStairs(self, n: int) -> int:
        nxt, nxt2 = 1, 1

        for i in range(n - 1):
            tmp = nxt
            nxt = nxt + nxt2
            nxt2 = tmp
        
        return nxt
