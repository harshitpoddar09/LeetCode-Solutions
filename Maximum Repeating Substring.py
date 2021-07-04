class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        res=0
        n=len(word)
        for i in range(len(sequence)):
            if sequence[i:i+n]==word:
                res+=1
        for j in range(res,-1,-1):
            if word*j in sequence:
                return j