class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        num=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                num.append(matrix[i][j])
        num.sort()
        return num[k-1]