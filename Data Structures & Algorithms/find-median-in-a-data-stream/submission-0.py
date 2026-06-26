from heapq import heapify, heappush, nsmallest

class MedianFinder:

    def __init__(self):
        # Median is middle most value of a SORTED list
        # When number number is added, median moves by 0.5 index
        # For example, if a list has 6 elements
        # the median is mean(3rd val/2 idx, 4th val/3 idx), effectively 3.5/2.5 idx
        # when a 7th element is added, 4th element becomes a median
        # As new values are added, we need to we need to keep them sorted
        # We can add 0.5 to the median index

        self.data = []
        heapify(self.data)
        self.medianIdx = 0

    def addNum(self, num: int) -> None:
        heappush(self.data, num)
        if len(self.data) == 1:
            self.medianIdx += 0.5
        self.medianIdx += 0.5

    def findMedian(self) -> float:
        res = 0

        if self.medianIdx % 1 == 0.5:
            a = nsmallest(int(self.medianIdx), self.data)[-1]
            b = nsmallest(int(self.medianIdx) + 1, self.data)[-1]
            res = (float(a) + float(b)) / 2
        else:
            res = nsmallest(int(self.medianIdx), self.data)[-1]
        # print("Median: ", float(res))
        return float(res)