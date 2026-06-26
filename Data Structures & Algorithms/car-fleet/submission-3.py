class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speedmap = {}   # [car_at_position]speed_of_car
        timereq = {}    # [car_at_position]steps_required_to_target
        fleets = 0

        for i, pos in enumerate(position):
            speedmap[pos] = speed[i]
        
        for pos in position:
            timereq[pos] = (target - pos) / speedmap[pos]

        position.sort(reverse=True)
        currFleet = []
        print(speedmap, timereq)
        for car in position:
            if len(currFleet) == 0:
                currFleet.append(car)
                continue
            
            nextCar = currFleet[-1]
            nextCarTime = timereq[nextCar]
            
            carTime = timereq[car]
            # print(f"curr {car}, next {nextCar}")
            if carTime <= nextCarTime:
                timereq[car] = timereq[nextCar]
                currFleet.append(car)
            else:
                fleets += 1
                print(f"fleet: {currFleet}")
                currFleet.clear()
                currFleet.append(car)
        if len(currFleet) > 0:
            fleets += 1
            print(f"fleet: {currFleet}")

        
        return fleets