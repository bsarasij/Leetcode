class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        m = len(firstList)
        n = len(secondList)
        if m == 0 or n == 0:
            return []
        i = 0
        j = 0
        results = []
        while i < m and j < n:
            first = max(firstList[i][0], secondList[j][0])
            second = min(firstList[i][1], secondList[j][1])
            if first <= second:
                results.append([first, second])
            if second == firstList[i][1]:
                i += 1
            else:
                j += 1
        return results
