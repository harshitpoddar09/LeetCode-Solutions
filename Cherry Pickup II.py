class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        d={}
        def cherry(x,y1,y2):
            if (x,y1,y2) not in d:
                if y1<0 or y1>=c or y2<0 or y2>=c:
                    return -inf
                ans=0
                ans+=grid[x][y1]
                if y1!=y2:
                    ans+=grid[x][y2]
                if x!=r-1:
                    ans+=max(cherry(x+1,new_y1,new_y2) for new_y1 in [y1,y1+1,y1-1] for new_y2 in [y2,y2+1,y2-1])
                d[(x,y1,y2)]=ans
            return d[(x,y1,y2)]
        return cherry(0,0,c-1) 