class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans=numBottles
        a=numBottles
        b=0
        while a>=numExchange:
            b=a%numExchange
            a=a//numExchange
            ans+=a
            a+=b
        return ans