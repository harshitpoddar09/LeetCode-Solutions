class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        ans=[0]*45   #largest sum of digits will be for the number 99999
        for i in range(lowLimit,highLimit+1):
            cur_sum=0
            while i!=0:
                cur_sum+=i%10
                i=i//10
            ans[cur_sum-1]+=1
        return max(ans)