class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count=0
        j=0
        for i in range(len(g)):
            while j<len(s):
                if g[i]<=s[j]:
                    count+=1
                    s.pop(j)
                    break
                j+=1
        return count