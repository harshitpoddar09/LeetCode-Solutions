from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        ans=0
        c=Counter(arr)
        freq=list(c.values())
        freq.sort()
        n=len(arr)
        cur=len(arr)
        while cur>n//2:
            ans+=1
            cur-=freq.pop()
        return ans