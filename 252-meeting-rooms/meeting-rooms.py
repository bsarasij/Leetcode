class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # if not intervals:
        #     return True
        intervals.sort()
        last_end = 0
        for start, end in intervals:
            if start < last_end:
                return False
            last_end = end
        return True