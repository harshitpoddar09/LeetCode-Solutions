class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        a=set(words1)
        b=set(words2)
        ans=0
        c=a.intersection(b)
        d1=Counter(words1)
        d2=Counter(words2)
        for i in c:
            if d1[i]==d2[i]==1:
                ans+=1
        return ans