class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        alpha=['a','b','c','d','e','f','g','h','i','j']
        n1=''
        for i in firstWord:
            n1+=str(alpha.index(i))
        n1=int(n1)
        n2=''
        for j in secondWord:
            n2+=str(alpha.index(j))
        n2=int(n2)
        n3=''
        for k in targetWord:
            n3+=str(alpha.index(k))
        n3=int(n3)
        return n1+n2==n3