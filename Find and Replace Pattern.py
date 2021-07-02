class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:     
        def match(a):
            b=[]
            ans=''
            for i in a:
                if i in b:
                    ans+=str(b.index(i))
                else:
                    ans+=str(len(b))
                    b.append(i)
            return ans
        pattern=match(pattern)
        ans=[]
        for j in words:
            if match(j)==pattern:
                ans.append(j)
        return ans