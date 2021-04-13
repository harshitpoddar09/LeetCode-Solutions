class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        indexes_j=[]
        indexes_i=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    indexes_j.append(j)
                    indexes_i.append(i)
        for j in indexes_j:
            for k in range(len(matrix)):
                matrix[k][j]=0
        for p in indexes_i:
            matrix[p]=[0]*len(matrix[p])