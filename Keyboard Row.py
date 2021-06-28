class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans=[]
        for j in words:
            a=j.lower()
            if all(i in "qwertyuiop" for i in a):
                ans.append(j)
            elif all(i in "asdfghjkl" for i in a):
                ans.append(j)
            elif all(i in "zxcvbnm" for i in a):
                ans.append(j)
        return ans