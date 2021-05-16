class Solution:
    def reformat(self, s: str) -> str:
        alpha=[]
        num=[]
        for i in s:
            if i.isalpha():
                alpha.append(i)
            else:
                num.append(i)
        ans=""
        if abs(len(alpha)-len(num))>1:
            return ans
        if len(alpha)>len(num):
            for j in range(len(num)):
                ans+=alpha[j]+num[j]
            ans+=alpha[-1]
        elif len(alpha)<len(num):
            for j in range(len(alpha)):
                ans+=num[j]+alpha[j]
            ans+=num[-1]
        else:
            for j in range(len(alpha)):
                ans+=num[j]+alpha[j]
        return ans