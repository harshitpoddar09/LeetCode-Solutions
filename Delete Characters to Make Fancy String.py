#Submission 2 - 800ms 17.2mb
class Solution:
    def makeFancyString(self, s: str) -> str:
        ch=list(s)
        ans=ch[0]
        for i in range(1,len(ch)-1):
            if ch[i-1]==ch[i]==ch[i+1]:
                ans+=''
            else:
                ans+=ch[i]
        if len(s)>1:
            ans+=ch[-1]
        return ans

#Submission 1 - 5420ms 20.1mb
class Solution:
    def makeFancyString(self, s: str) -> str:
        ch=list(s)
        idx=[]
        for i in range(1,len(ch)-1):
            if ch[i-1]==ch[i]==ch[i+1]:
                idx.append(i-1)
        for j in idx[::-1]:
            ch.pop(j)
        return ''.join(ch)