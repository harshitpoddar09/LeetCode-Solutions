class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans=[]
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j]<=prices[i]:
                    amount=prices[i]-prices[j]
                    break
            else:
                amount=prices[i]
            ans.append(amount)
        return ans