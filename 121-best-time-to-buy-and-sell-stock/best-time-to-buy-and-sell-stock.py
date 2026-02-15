class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minCost = float('inf')
        maxProf = 0
        for i in range(len(prices)):
            if prices[i] < minCost:
                minCost = prices[i]
            maxProf = max(maxProf, prices[i] - minCost) 
        return maxProf if maxProf > 0 else 0