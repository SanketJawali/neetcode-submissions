class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # MISTAKE: Trying to be Greedy by selecting largest coin first
        memo = {}

        def helper(curr: int):
            if curr == amount:
                return 0
            if curr in memo:
                return memo[curr]
            
            m = float("inf")
            for c in coins:
                if (c + curr) > amount:
                    continue
                need = helper(curr + c)
                if need >= 0:
                    m = min(m, 1 + need) if m > 0 else 1 + need
            memo[curr] = m
            return m
        res = helper(0)
        return res if res < float("inf") else -1
