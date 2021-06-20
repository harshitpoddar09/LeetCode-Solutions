class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        minimum=prices[0]
        for i in range(1,len(prices)):
            profit=max(profit,prices[i]-minimum)
            minimum=min(minimum,prices[i])
        return profit