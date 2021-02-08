class Solution:
    def isPathCrossing(self, path: str) -> bool:
        ans=0
        point=[[0,0]]
        current=[0,0]
        for i in path:
            if i=='N':
                current=[current[0],current[1]+1]
            elif i=='E':
                current=[current[0]+1,current[1]]
            elif i=='S':
                current=[current[0],current[1]-1]
            elif i=='W':
                current=[current[0]-1,current[1]]
            if current in point:
                ans=1
                break
            else:
                point.append(current)
        return ans