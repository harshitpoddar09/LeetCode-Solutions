from collections import Counter 
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d=Counter(arr)
        k-=1
        for i in arr:
            if d[i]==1:
                if k:
                    k-=1
                else:
                    return i
        return ''