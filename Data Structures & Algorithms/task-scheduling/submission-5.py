from heapq import heapify_max, heappop_max, heappush_max
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        timeline = []

        # Get the frequency count for each task
        for t in tasks: # O(n)
            if t not in freq:
                freq[t] = 1
                continue
            freq[t] += 1
        # Initially add all tasks along with their freq in heap
        heap = [(n, task) for task, n in freq.items()]
        heapify_max(heap)   # O(n)

        waitlist = {}

        while not (len(heap) == 0 and len(waitlist) == 0):
            # Len of timeline is also equal to out number of cycles
            # We are appending something for each loop iteration
            # therefore len(timeline) is always equal to time
            if len(heap) < 1:
                timeline.append("idle")
            else:
                freq, task = heappop_max(heap)
                timeline.append(task)
                freq -= 1
                # Set the timer of when this element can enter the heap again
                if not freq == 0:
                    waitlist[len(timeline) + n] = (freq, task)

            # Check for any task can be added to heap again
            time = len(timeline)
            if time in waitlist:
                heappush_max(heap, waitlist[time])
                del waitlist[time]
            # print(timeline, heap, waitlist)

        return len(timeline)