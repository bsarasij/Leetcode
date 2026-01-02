class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        arrows = 1
        min_prev = points[0][1]
        for i in range(1,len(points)):
            if points[i][0] > min_prev:
                arrows +=  1
                min_prev = points[i][1]
            else:
                min_prev = min(min_prev, points[i][1])
        return arrows
