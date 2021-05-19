class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1)>=len(str2):
            if str2*(len(str1)//len(str2))==str1:
                return str2
            for i in range(len(str2)//2,0,-1):
                if str2[:i]*(len(str2)//i)==str2 and str2[:i]*(len(str1)//i)==str1:
                    return str2[:i]
            return ''
        else:
            if str1*(len(str2)//len(str1))==str2:
                return str1
            for i in range(len(str1)//2,0,-1):
                if str1[:i]*(len(str1)//i)==str1 and str1[:i]*(len(str2)//i)==str2:
                    return str1[:i]
            return ''