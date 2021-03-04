class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        a=sorted(score,reverse=True)
        ans=[]
        for i in score:
            if a.index(i)==0:
                ans.append('Gold Medal')
            elif a.index(i)==1:
                ans.append('Silver Medal')
            elif a.index(i)==2:
                ans.append('Bronze Medal')
            else:
                ans.append(str(a.index(i)+1))
        return ans