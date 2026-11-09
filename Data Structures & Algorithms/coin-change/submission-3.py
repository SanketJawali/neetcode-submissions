class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Instead of calculating coins needed for an amount
        # we calculate coins needed for all amounts in range [1, amount]
        # We can use the previously calculated values in memo as cache

        memo = [float("inf")] * (amount + 1)
        memo[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    memo[i] = min(memo[i], 1 + memo[i - c])
            
        
        return memo[amount] if memo[amount] != float("inf") else -1