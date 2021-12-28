class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        a=0
        ans=0
        for i in range(len(values)):
            ans=max(ans,a+values[i]-i)
            a=max(a,values[i]+i)
        return ans