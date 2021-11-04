class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        ans=0
        rungs.insert(0,0)
        i=1
        while i<len(rungs):
            a=rungs[i]-rungs[i-1]
            if a>dist:
                if a/dist==a//dist:
                    ans+=(a//dist)-1
                else:
                    ans+=a//dist
            i+=1
        return ans