class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle=[[1]]
        if rowIndex>0:
            triangle=[[1],[1,1]]
        for i in range(2,rowIndex+1):
            a=[1]
            for j in range(len(triangle[i-1])-1):
                a.append(triangle[i-1][j]+triangle[i-1][j+1])
            a.append(1)
            triangle.append(a)
        return triangle[-1]