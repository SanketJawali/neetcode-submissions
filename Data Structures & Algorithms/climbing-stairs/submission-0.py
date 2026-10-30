class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def climb(step: int, count: int):
            if step == n:
                return count + 1
            if step in memo:
                return memo[step]
            
            step1 = step2 = 0
            step1 = climb(step + 1, count)
            if step + 2 <= n:
                step2 = climb(step + 2, count)
            memo[step] = step1 + step2
            return step1 + step2
        
        return climb(0, 0)