from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=Counter(nums)
        sorted_d=sorted(d.items(),key=lambda k:k[1],reverse=True)
        ans=[]
        for key,val in sorted_d:
            if k==0:
                break
            ans.append(key)
            k-=1
        return ans