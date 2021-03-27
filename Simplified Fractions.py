class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans=[]
        fraction=[]
        for i in range(2,n+1):
            for j in range(1,i):
                if j/i not in fraction:
                    ans.append(str(j)+'/'+str(i))
                    fraction.append(j/i)
        return ans