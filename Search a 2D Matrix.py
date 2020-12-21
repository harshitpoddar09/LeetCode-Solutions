class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                num.append(matrix[i][j])
        for p in num:
            if p==target:
                return 'true'
        else:
            print('false')