import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        rate = piles[-1]
        l, r = 1, rate
        k = piles[-1]   # Set to max initially

        while l <= r:
            rate = (l + r) // 2
            hrs = 0

            for pile in piles:
                hrs += math.ceil(pile/rate)
            
            # If hrs within h set k, else find new
            if hrs > h:
                l = rate + 1
            elif hrs <= h:
                k = min(k, rate)
                r = rate - 1

        return k