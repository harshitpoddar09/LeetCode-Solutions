class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        l=len(s)
        prefix=''
        i=0
        while len(prefix)<l and i<len(words):
            prefix+=words[i]
            i+=1
        return s==prefix