class Solution:
    def reverseWords(self, s: str) -> str:
        a=s.split()
        ans=str()
        for i in a[::-1]:
            ans+=i+' '
        return ans[:len(ans)-1]