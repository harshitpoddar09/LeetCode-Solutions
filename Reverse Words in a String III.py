class Solution:
    def reverseWords(self, s: str) -> str:
        words=list(s.split())
        for i in range(len(words)):
            words[i]=words[i][::-1]
        return ' '.join(words)