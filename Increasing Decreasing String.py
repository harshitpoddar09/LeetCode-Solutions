class Solution:
    def sortString(self, s: str) -> str:
        char=[]
        char[:0]=s
        ans=''
        while len(char)>0:
            for i in sorted(set(char)):
                ans+=i
                char.remove(i)
            for j in sorted(set(char),reverse=True):
                ans+=j
                char.remove(j)
        return ans