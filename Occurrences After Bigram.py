class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ans=[]
        text=text.split()
        for i in range(len(text)-2):
            if text[i]==first and text[i+1]==second:
                ans.append(text[i+2])
        return ans