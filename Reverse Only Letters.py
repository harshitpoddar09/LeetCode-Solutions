class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        S_rev=S[::-1]
        for i in S_rev:
            if not ((ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122)):
                S_rev=S_rev.replace(i,'')
        j=0
        ans=''
        for k in S:
            if not ((ord(k)>=65 and ord(k)<=90) or (ord(k)>=97 and ord(k)<=122)):
                ans+=k
            else:
                ans+=S_rev[j]
                j+=1
        return ans