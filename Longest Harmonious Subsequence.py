#Submission 3 - 292 ms
from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d=Counter(nums)
        ans=0
        for i in d:
            if i+1 in d:
                ans=max(ans,d[i]+d[i+1])
        return ans

#Submission 2 - 292 ms
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        ans=0
        for i in d:
            if i+1 in d:
                ans=max(ans,d[i]+d[i+1])
        return ans

#Submission 1 - 312 ms
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        a=sorted(d)
        ans=0
        for i in range(len(a)-1):
            if a[i]+1==a[i+1]:
                ans=max(ans,d[a[i]]+d[a[i+1]])
        return ans