#Submission 2 - 66ms
class Solution:
    def myAtoi(self, s: str) -> int:
        i=0
        m=1
        cur=''
        while i<len(s) and s[i]==' ':
            i+=1
        if i<len(s) and s[i]=='+':
            m=1
            i+=1
        elif i<len(s) and s[i]=='-':
            m=-1
            i+=1
        while i<len(s) and s[i].isdigit():
            cur+=s[i]
            i+=1
        if cur=='':
            return 0
        ans=int(cur)*m
        if ans>(2**31)-1:
            return (2**31)-1
        elif ans<-(2**31):
            return -(2**31)
        else:
            return ans

#Submission 1 - 78ms
class Solution:
    def myAtoi(self, s: str) -> int:
        i=0
        while i<len(s):
            if s[i]!=' ':
                break
            i+=1
        if i==len(s):
            return 0
        cur=''
        f=False
        m=1
        while i<len(s):
            if s[i].isdigit():
                cur+=s[i]
            elif cur=='':
                if s[i]=='+':
                    if not f:
                        m=1
                        f=True
                        i+=1
                        continue
                    else:
                        return 0
                elif s[i]=='-':
                    if not f:
                        m=-1
                        f=True
                        i+=1
                        continue
                    else:
                        return 0
                else:
                    break
            else:
                break
            i+=1
        if cur=='':
            return 0
        ans=int(cur)*m
        if ans>(2**31)-1:
            return (2**31)-1
        elif ans<-(2**31):
            return -(2**31)
        else:
            return ans