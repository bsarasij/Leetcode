class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        result = []
        i, j = 0, 0
        while i < len(slots1) and j < len(slots2):
            s1, e1 = slots1[i][0], slots1[i][1]
            s2, e2 = slots2[j][0], slots2[j][1]
            start = max(s1, s2)
            end = min(e1, e2)

            if end - start >= duration:
                return [start, start + duration]
            if e1 < e2:
                i += 1
            else:
                j += 1

        return result