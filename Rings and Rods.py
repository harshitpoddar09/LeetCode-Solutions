#Submission 2 - 21ms
class Solution:
    def countPoints(self, rings: str) -> int:
        d={}
        for i in range(0,len(rings),2):
            idx=rings[i+1]
            if idx not in d:
                d[idx]=set()
            d[idx].add(rings[i])
        return sum(len(d[key])==3 for key in d)

#Submission 1 - 88ms
class Solution:
    def countPoints(self, rings: str) -> int:
        d={}
        for i in range(0,len(rings),2):
            idx=rings[i+1]
            if idx not in d:
                d[idx]=set()
            d[idx].add(rings[i])
        ans=0
        for key in d:
            if len(d[key])==3:
                ans+=1
        return ans