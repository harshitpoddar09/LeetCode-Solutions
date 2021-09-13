#SUBMISSION 2 - 64ms
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        ans=0
        ans+=sum(ele>0 for row in grid for ele in row)
        ans+=sum(max(row) for row in grid)
        ans+=sum(max(col) for col in zip(*grid))
        return ans

#SUBMISSION 1 - 84ms
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        ans=0
        for row in range(len(grid)):
            row_max=0
            for col in range(len(grid[0])):
                if grid[row][col]>0:
                    ans+=1
                row_max=max(row_max,grid[row][col])
            ans+=row_max
        for col in range(len(grid[0])):
            col_max=0
            for row in range(len(grid)):
                col_max=max(col_max,grid[row][col])
            ans+=col_max
        return ans