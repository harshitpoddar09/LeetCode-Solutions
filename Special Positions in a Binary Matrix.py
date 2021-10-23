#SUBMISSION 2 - 172ms
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        def sum_col(mat,c):
            sc=0
            for row in range(len(mat)):
                sc+=mat[row][c]
            return sc
        ans=0
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col]==1 and sum(mat[row])==1 and sum_col(mat,col)==1:
                    ans+=1
        return ans

#SUBMISSION 1 - 345ms
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        def check(mat,r,c):
            c1=0
            for i in mat[r]:
                if i==1:
                    c1+=1
                if c1>1:
                    return False
            c2=0
            for row in range(len(mat)):
                if mat[row][c]==1:
                    c2+=1
                if c2>1:
                    return False
            return True
        ans=0
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col]==1 and check(mat,row,col):
                    ans+=1
        return ans