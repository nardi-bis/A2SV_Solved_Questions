class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash = 0
        hold = -prices[0]#bought on day 0

        for price in prices[1:]:
            cash = max(cash, hold + price - fee) #sell today
            hold = max(hold, cash - price)#buy today

        return cash