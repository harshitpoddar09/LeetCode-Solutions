class Solution:
    def maxDepth(self, s: str) -> int:
        ans=0
        count=0
        for i in s:
            if i=='(':
                count+=1
            elif i==')':
                count-=1
            ans=max(ans,count)
        return ans