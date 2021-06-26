class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split()
        ans=['']*len(s)
        for i in s:
            ans[int(i[-1])-1]+=i[:len(i)-1]
        return ' '.join(ans)