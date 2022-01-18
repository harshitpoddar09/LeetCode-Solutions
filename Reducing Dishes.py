class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        ans=0
        satisfaction.sort(reverse=True)
        cur=0
        prefix=0
        for i in satisfaction:
            cur+=prefix+i
            ans=max(ans,cur)
            prefix+=i
        return ans