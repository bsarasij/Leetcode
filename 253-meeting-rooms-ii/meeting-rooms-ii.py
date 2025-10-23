class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        events = []
        for start, end in intervals:
            events.append([start, 1])
            events.append([end, -1])
        
        events.sort(key = lambda x: (x[0], x[1]) )
        conf = 0
        max_conf = 0
        # print(events)
        for event in events:
            conf += event[1]
            # print(conf)
            max_conf = max(max_conf, conf)
        return max_conf