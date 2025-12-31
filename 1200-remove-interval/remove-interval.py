class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        results = []
        for intv in intervals:
            if intv[1] < toBeRemoved[0] or intv[0] > toBeRemoved[1]:
                results.append(intv)
            
            else:
                if intv[0] < toBeRemoved[0]:
                    results.append([intv[0], toBeRemoved[0]])
                if toBeRemoved[1] < intv[1]:
                    results.append([toBeRemoved[1], intv[1]])
            
        return results
