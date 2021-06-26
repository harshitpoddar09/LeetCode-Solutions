from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        freqDict=Counter(s)
        ans=0
        odd=0
        for key,value in freqDict.items():
            if value%2==0:
                ans+=value
            else:
                ans+=value-1
                odd+=1
        return ans+min(odd,1)