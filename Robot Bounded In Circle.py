class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x=y=0
        dx=0
        dy=1
        for i in instructions:
            if i=='L':
                dx,dy=-dy,dx
            elif i=='R':
                dx,dy=dy,-dx
            else:
                x+=dx
                y+=dy
        return (x,y)==(0,0) or (dx,dy)!=(0,1)