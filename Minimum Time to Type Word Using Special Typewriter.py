class Solution:
    def minTimeToType(self, word: str) -> int:
        ans=0
        cur='a'
        for i in word:
            dist=abs(ord(cur)-ord(i))
            dist=min(dist,26-dist)
            ans+=dist+1
            cur=i
        return ans