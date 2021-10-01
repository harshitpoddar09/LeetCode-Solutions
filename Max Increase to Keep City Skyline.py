class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        h1=[max(row) for row in grid]
        h2=[max(col) for col in zip(*grid)]
        ans=0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                ans+=max(min(h1[row],h2[col])-grid[row][col],0)
        return ans