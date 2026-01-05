class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        maxHeight = heights[-1]
        results = []
        results.append(len(heights) - 1)
        for i in reversed(range(len(heights)-1)):
            if heights[i] > maxHeight:
                results.append(i)
                maxHeight = heights[i]
        return results[::-1]