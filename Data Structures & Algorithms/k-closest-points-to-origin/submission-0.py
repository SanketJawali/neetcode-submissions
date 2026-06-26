import math
from heapq import heapify, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(self.calcDistance(point), point) for point in points]
        heapify(distances)

        result = []
        for _ in range(k):
            _, point = heappop(distances)
            result.append(point)
        return result
            
    def calcDistance(self, point: List[int]) -> float:
        x, y = point[0], point[1]
        return math.sqrt(x**2 + y**2)