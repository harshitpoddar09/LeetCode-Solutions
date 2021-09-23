class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text=text.split()
        brokenLetters=set(brokenLetters)
        ans=0
        for i in text:
            for j in i:
                if j in brokenLetters:
                    break
            else:
                ans+=1
        return ans