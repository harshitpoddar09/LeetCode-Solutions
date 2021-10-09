from collections import Counter
class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        d=Counter(A)
        A=sorted(A,key=abs)
        for i in A:
            if d[i]==0:
                continue
            if d[2*i]==0:
                return False
            d[i]-=1
            d[2*i]-=1
        return True