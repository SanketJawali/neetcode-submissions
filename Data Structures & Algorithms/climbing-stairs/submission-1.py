class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1 # Number of steps we can take from current step

        for i in range(n - 1):
            one, two = one + two, one
        
        return one