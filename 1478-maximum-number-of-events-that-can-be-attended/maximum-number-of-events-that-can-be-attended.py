import heapq
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        maxEv = 0
        events.sort()
        numEv = len(events)
        min_heap = []
        i = 0
        day = 0
        while i < numEv or min_heap:
            if not min_heap:
                day = max(day,events[i][0])
            while i < numEv and events[i][0] <= day:
                heapq.heappush(min_heap, events[i][1])
                i += 1
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)
            if min_heap:
                heapq.heappop(min_heap)
                maxEv += 1
                day += 1
        return maxEv
             