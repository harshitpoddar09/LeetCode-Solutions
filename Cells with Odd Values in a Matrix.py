class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        matrix=[[0 for i in range(m)] for j in range(n)]
        for i in indices:
            for p in range(len(matrix[i[0]])):
                matrix[i[0]][p]+=1
            for q in range(len(matrix)):
                matrix[q][i[1]]+=1
        count=0
        for j in matrix:
            for k in j:
                if k%2!=0:
                    count+=1
        return count