class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        length=0
        for i in range(len(words)):
            a=chars
            length+=len(words[i])
            for j in words[i]:
                if j not in a:
                    length-=len(words[i])
                    break
                else:
                    a=a.replace(j,'',1)
        return length            