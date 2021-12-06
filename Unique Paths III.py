class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        empty=1
        r=len(grid)
        c=len(grid[0])
        x=0
        y=0
        for i in range(r):
            for j in range(c):
                ele=grid[i][j]
                if ele==0:
                    empty+=1
                if ele==1:
                    x=i
                    y=j
        self.ans=0
        def paths(row,col,covered,grid):
            if row<0 or col<0 or row>r-1 or col>c-1 or grid[row][col]==-1:
                return 
            if grid[row][col]==2:
                if covered==empty:
                    self.ans+=1
                return
            grid[row][col]=-1
            paths(row-1,col,covered+1,grid)
            paths(row+1,col,covered+1,grid)
            paths(row,col-1,covered+1,grid)
            paths(row,col+1,covered+1,grid)
            grid[row][col]=0
        paths(x,y,0,grid)
        return self.ans