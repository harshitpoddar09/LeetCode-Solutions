class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans=0
        for i in sentences:
            words=i.count(' ')
            ans=max(ans,words)
        return ans+1