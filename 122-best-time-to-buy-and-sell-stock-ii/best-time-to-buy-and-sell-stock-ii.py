class Solution:
    def simDay(self, index, buy, prices, n, dp):
        if index == n:
            return 0
        profit = 0
        if dp[index][buy] != -1:
            return dp[index][buy]

        if buy:
            profit = max(-prices[index] + self.simDay(index + 1, 0, prices, n, dp), 0 + self.simDay(index + 1, 1, prices, n, dp))
        else:
            profit = max(prices[index] + self.simDay(index + 1, 1, prices, n, dp), 0 + self.simDay(index + 1, 0, prices, n, dp))
        
        dp[index][buy] = profit
        return profit


    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1 for j in range(2)] for i in range(n)]
        maxProf = self.simDay(0, 1, prices, n, dp)
        return maxProf
