class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        d={}
        n=len(words)
        for i in words:
            for j in i:
                if j in d:
                    d[j]+=1
                else:
                    d[j]=1
        for key,value in d.items():
            if value%n!=0:
                return False
        return True