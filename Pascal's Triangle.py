class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[[1]]
        if numRows>=2:
            ans.append([1,1])
        for i in range(2,numRows):
            a=[1]
            for j in range(len(ans[i-1])-1):
                a.append(ans[i-1][j]+ans[i-1][j+1])
            a.append(1)
            ans.append(a)
        return ans