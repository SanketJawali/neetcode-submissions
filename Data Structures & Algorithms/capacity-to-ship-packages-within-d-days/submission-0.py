class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        capacity = sum(weights)
        low, high = max(weights), sum(weights)

        while low <= high:
            mid = low + ((high - low) // 2)

            ship = mid  # Ship with mid capacity
            d = 1
            for i, w in enumerate(weights):
                if ship >= w:
                    ship -= w
                else:
                    # Next day
                    d += 1
                    ship = mid - w
            
            if d > days:
                low = mid + 1
            elif d <= days:
                high = mid - 1
                capacity = min(capacity, mid)
        return capacity