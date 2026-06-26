class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        times = []
        
        for i, pos in enumerate(position):
            times.append((target - pos) / speed[i])

        cars = list(zip(position, speed, times))
        cars.sort(reverse=True)

        fleetTime = 0
        for p, _, t in cars:
            if fleetTime == 0:
                fleetTime = t
            if t > fleetTime:
                fleets.append(fleetTime)
                fleetTime = t
        if not fleetTime == 0:
            fleets.append(fleetTime)
        
        return len(fleets)