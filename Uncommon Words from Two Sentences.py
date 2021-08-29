#Submission 2 - 32 ms
from collections import Counter
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        A=A.split()
        B=B.split()
        d1=Counter(A)
        d2=Counter(B)
        ans=[]
        for p in d1:
            if d1[p]==1 and p not in d2:
                ans.append(p)
        for q in d2:
            if d2[q]==1 and q not in d1:
                ans.append(q)
        return ans

#Submission 1 - 24 ms
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        d1={}
        d2={}
        A=A.split()
        B=B.split()
        ans=[]
        for i in A:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1
        for j in B:
            if j in d2:
                d2[j]+=1
            else:
                d2[j]=1
        for p in d1:
            if d1[p]==1 and p not in d2:
                ans.append(p)
        for q in d2:
            if d2[q]==1 and q not in d1:
                ans.append(q)
        return ans