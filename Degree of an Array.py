from collections import Counter
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d=Counter(nums)
        val=0
        ele=[]
        for key in d:
            if d[key]>val:
                val=d[key]
                ele=[key]
            elif d[key]==val:
                ele.append(key)
        ans=float('inf')
        for i in ele:
            a=nums.index(i)
            b=nums[::-1].index(i)
            c=len(nums)-b
            ans=min(ans,c-a)
        return ans