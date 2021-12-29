#Submission 2 - 892ms
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans=''
        i=j=0
        while i<len(s) and j<len(spaces):
            if i==spaces[j]:
                ans+=' '
                j+=1
            ans+=s[i]
            i+=1
        if i<len(s):
            ans+=s[i:]
        return ans

#Submission 1 - 6336ms
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces.reverse()
        ans=''
        for i in spaces:
            ans=' '+s[i:]+ans
            s=s[:i]
        if i!=0:
            ans=s+ans
        return ans