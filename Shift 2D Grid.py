class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        for i in range(k):
            grid[0].insert(0,grid[m-1][n-1])
            for j in range(m-1):
                grid[j+1].insert(0,grid[j][n])
                grid[j].pop()
            grid[m-1].pop()
        return grid