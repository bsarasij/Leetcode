class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0 
        last_end = - float('inf')
        intervals.sort(key = lambda x : x[1])
        for start, end in intervals:
            if start >= last_end:
                count += 1
                last_end = end
        return len(intervals) - count