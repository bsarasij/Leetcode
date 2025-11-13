class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minCost = float('inf')
        for i in range(len(prices)):
            minCost = min(minCost, prices[i])
            maxProfit = max(maxProfit, prices[i] - minCost)
        return maxProfit