class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        results = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            results.append(intervals[i])
            i += 1

        start, end = newInterval[0], newInterval[1] 
        while i < n and newInterval[1] >= intervals[i][0]:
            start = min(intervals[i][0], start)
            end = max(intervals[i][1], end)
            i += 1
        results.append([start, end])
        if i < n:
            results.extend(intervals[i:])
        return results
        

        