class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort()
        sorted_int = []
        sorted_int.append(intervals[0])
        for j in range(1, len(intervals)):
            if sorted_int[-1][1] >= intervals[j][0]:
                sorted_int[-1][0] = min(sorted_int[-1][0], intervals[j][0])
                sorted_int[-1][1] = max(sorted_int[-1][1], intervals[j][1])
            else:
                sorted_int.append(intervals[j])
        return sorted_int
                