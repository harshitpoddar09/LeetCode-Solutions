class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1)!=len(s2):
            return 0
        w1=[]
        w2=[]
        count=0
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                count+=1
                w1.append(s1[i])
                w2.append(s2[i])
        if count>2:
            return 0
        return sorted(w1)==sorted(w2)