class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        n = len(prices)
        for i in range(n):
            profit = max(prices[i:]) - prices[i]
            best = max(best, profit)
        return best