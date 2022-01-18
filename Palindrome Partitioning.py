class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def process(ans,cur,s):
            if s=='':
                ans.append(cur)
            for i in range(len(s)):
                if s[:i+1]==s[:i+1][::-1]:
                    process(ans,cur+[s[:i+1]],s[i+1:])
        if s=='':
            return [[]]
        ans=[]
        process(ans,[],s)
        return ans