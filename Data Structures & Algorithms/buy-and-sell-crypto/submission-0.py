class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            if maxP < sell-minBuy:
                maxP = sell - minBuy
            minBuy = min(minBuy, sell)
        return maxP