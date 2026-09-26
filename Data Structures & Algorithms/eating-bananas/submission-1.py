import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        res = high

        def calchrs(k: int):
            hrs = 0
            for p in piles:
                hrs += math.ceil(p / k)
            return hrs

        while low <= high:
            # Calculate hours required
            mid = low + ((high - low) // 2)
            hrs = calchrs(mid)

            if hrs > h:
                low = mid + 1
                print(low, mid, high)
            elif hrs <= h:
                high = mid - 1
                res = min(res, mid)
                print(low, mid, high)
        return res