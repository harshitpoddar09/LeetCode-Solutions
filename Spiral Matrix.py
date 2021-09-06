class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        t=0
        b=len(matrix)-1
        l=0
        r=len(matrix[0])-1
        direc=0
        ans=[]
        while t<=b and l<=r:
            if direc==0:
                for i in range(l,r+1):
                    ans.append(matrix[t][i])
                t+=1
                direc=1
            elif direc==1:
                for i in range(t,b+1):
                    ans.append(matrix[i][r])
                r-=1
                direc=2
            elif direc==2:
                for i in range(r,l-1,-1):
                    ans.append(matrix[b][i])
                b-=1
                direc=3
            elif direc==3:
                for i in range(b,t-1,-1):
                    ans.append(matrix[i][l])
                l+=1
                direc=0
        return ans