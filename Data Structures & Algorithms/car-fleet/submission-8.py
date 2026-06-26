class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        times = []
        
        for i, pos in enumerate(position):
            times.append((target - pos) / speed[i])

        cars = sorted(
            list(zip(position, times)),
            reverse=True
        )

        fleetTime = 0
        for p, t in cars:
            if fleetTime == 0:
                fleetTime = t
            if t > fleetTime:
                fleets += 1
                fleetTime = t
        fleets += 1 # Add final fleet
        
        return fleets