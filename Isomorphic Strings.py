class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1={}
        s1=''
        j=1
        for i in s:
            if i in d1:
                s1+=d1[i]
            else:
                d1[i]=str(j)
                j+=1
                s1+=d1[i]
        d2={}
        t1=''
        k=1
        for i in t:
            if i in d2:
                t1+=d2[i]
            else:
                d2[i]=str(k)
                k+=1
                t1+=d2[i]
        return s1==t1