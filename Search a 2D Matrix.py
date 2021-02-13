#Method1
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
            
#Method2
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ans=0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==target:
                    ans=1
                    break
        return ans
