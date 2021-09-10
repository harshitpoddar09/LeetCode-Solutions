class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(len(A)):
            A[i]=A[i][::-1]
            for j in range(len(A[i])):
                if A[i][j]==1:
                    A[i][j]=0
                else:
                    A[i][j]=1
        return A