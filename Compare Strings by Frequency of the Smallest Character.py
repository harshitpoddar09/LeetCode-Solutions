from collections import Counter
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        freqw=[]
        for i in words:
            d=Counter(i)
            freqw.append(d[min(d)])
        freqq=[]
        for j in queries:
            d=Counter(j)
            freqq.append(d[min(d)])
        ans=[]
        for q in freqq:
            c=0
            for w in freqw:
                if w>q:
                    c+=1
            ans.append(c)
        return ans