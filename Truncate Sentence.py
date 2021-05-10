class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words=list(s.split())
        return ' '.join(words[:k])