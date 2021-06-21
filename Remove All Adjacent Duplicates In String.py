#Submission3 - 76ms
class Solution:
    def removeDuplicates(self, s: str) -> str:
        ans=[s[0]]
        for i in range(1,len(s)):
            if ans and s[i]==ans[-1]:
                ans.pop()
            else:
                ans.append(s[i])
        return ''.join(ans)

#Submission2 - 88ms
class Solution:
    def removeDuplicates(self, s: str) -> str:
        if len(s)<=1:
            return s
        ans=[]
        for i in range(len(s)):
            ans.append(s[i])
            if len(ans)>1 and ans[-1]==ans[-2]:
                ans.pop()
                ans.pop()
        return ''.join(ans)

#Submission1 - 124ms
class Solution:
    def removeDuplicates(self, s: str) -> str:
        if len(s)<=1:
            return s
        a=[]
        a[:0]=s
        i=0
        while i<len(a)-1:
            if a[i]==a[i+1]:
                a.pop(i)
                a.pop(i)
                if i>0:
                    i-=1
            else:
                i+=1
        return ''.join(a)