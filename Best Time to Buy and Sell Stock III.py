class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1=float('inf')
        buy2=float('inf')
        sell1=0
        sell2=0
        for i in prices:
            buy1=min(buy1,i)
            sell1=max(sell1,i-buy1)
            buy2=min(buy2,i-sell1)
            sell2=max(sell2,i-buy2)
        return sell2