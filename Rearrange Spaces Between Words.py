class Solution:
    def reorderSpaces(self, text: str) -> str:
        count=0
        for i in text:
            if i==' ':
                count+=1
        words=list(text.split())
        if len(words)==1:
            return words[0]+(' '*count)
        a=count//(len(words)-1)
        b=count%(len(words)-1)
        ans=''
        for j in range(len(words)-1):
            ans+=words[j]+(' '*a)
        ans+=words[-1]+(' '*b)
        return ans