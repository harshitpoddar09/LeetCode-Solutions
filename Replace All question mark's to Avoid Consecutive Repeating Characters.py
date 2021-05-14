class Solution:
    def modifyString(self, s: str) -> str:
        alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for i in range(len(s)):
            if s[i]=='?':
                if i-1>=0 and i+1<len(s):
                    for j in alphabets:
                        if s[i-1]!=j and s[i+1]!=j:
                            s=s.replace(s[i],j,1)
                            break
                elif i-1<0 and i+1<len(s):
                    for j in alphabets:
                        if s[i+1]!=j:
                            s=s.replace(s[i],j,1)
                            break
                elif i-1>=0 and i+1>=len(s):
                    for j in alphabets:
                        if s[i-1]!=j:
                            s=s.replace(s[i],j,1)
                            break
                else:
                    s=s.replace(s[i],'a',1)
        return s