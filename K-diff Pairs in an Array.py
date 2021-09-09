from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ans=0
        if k==0:
            d=Counter(nums)
            for i in d:
                if d[i]>1:
                    ans+=1
            return ans
        nums=set(nums)
        for i in nums:
            if i-k in nums:
                ans+=1
        return ans