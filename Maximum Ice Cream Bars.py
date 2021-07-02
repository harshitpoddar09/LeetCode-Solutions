class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs=sorted(costs)
        i=0
        ans=0
        while i<len(costs) and coins>0:
            coins-=costs[i]
            i+=1
            ans+=1
        if coins<0:
            return ans-1
        return ans