class Solution:
    def countLargestGroup(self, n: int) -> int:
        d={}
        for i in range(1,n+1):
            a=0
            for j in str(i):
                a+=int(j)
            if a in d:
                d[a]+=1
            else:
                d[a]=1
        keymax=max(d, key=lambda x:d[x])
        valmax=d[keymax]
        ans=0
        for key,value in d.items():
            if value==valmax:
                ans+=1
        return ans