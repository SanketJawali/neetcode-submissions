class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        postime = [0] * len(position)

        # Calculate time required for each car to reach target, by itself
        for i in range(len(position)):
            t = (target - position[i]) / speed[i]
            postime[i] = (position[i], t)
        # Sort by distance from the target
        postime.sort(reverse=True)

        # Iterate through cars starting from cars closest to the target
        fleets = 0
        for i in range(len(postime)):
            # Current
            p, t = postime[i]
            if i == 0: 
                fleets += 1
                continue
            # Car ahead
            ap, at = postime[i - 1]
            if t <= at:
                # Current car part of current fleet
                postime[i] = (p, at)
            else:
                # New fleet, can't catch up to fleet ahead
                fleets += 1
        
        return fleets
