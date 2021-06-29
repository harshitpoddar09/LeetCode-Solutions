class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        left=0
        right=len(mat)-1
        ans=0
        for i in range(len(mat)):
            ans+=mat[i][left]+mat[i][right]
            left+=1
            right-=1
        if len(mat)%2!=0:
            ans-=mat[len(mat)//2][len(mat)//2]
        return ans