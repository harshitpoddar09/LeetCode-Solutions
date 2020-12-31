class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        ans=0
        if word.isupper():
            ans=1
        elif word.islower():
            ans=1
        elif word[0].isupper() and word[1:].islower():
            ans=1
        return ans==1