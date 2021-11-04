class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word)):
            if word[i]==ch:
                break
        if i<len(word)-1:
            return word[i::-1]+word[i+1:]
        elif word[i]==ch:
            return word[::-1]
        else:
            return word