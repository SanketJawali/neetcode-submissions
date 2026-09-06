class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [B1, S7, 2, 1, B1, S4, B3, S6]
        a, b = 0, 1
        res = 0
        owns = (False, 0) # (Owns stock?, price)

        for a in range(len(prices)):
            own, value = owns
            if a == len(prices) - 1:
                # Sell
                if own:
                    res += prices[a] - value
                    print("Sold ", prices[a])
                return res
            # Check for bull/bear
            if prices[b] > prices[a]:
                # Buy only if we don't own currently
                if not own:
                    owns = (True, prices[a])
                    print("Bought ", prices[a])
            elif prices[b] < prices[a]:
                # Sell
                if own:
                    res += prices[a] - value
                    owns = (False, 0)
                    print("Sold ", prices[a])
            b += 1