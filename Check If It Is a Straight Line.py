class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        ans=1
        if coordinates[0][0]!=coordinates[1][0]:
            m=(coordinates[0][1]-coordinates[1][1])/(coordinates[0][0]-coordinates[1][0])
        else:
            for j in coordinates:
                if j[0]!=coordinates[0][0]:
                    ans=0
                    break
            return ans
        for i in range(2,len(coordinates)):
            if coordinates[0][0]==coordinates[i][0]:
                ans=0
                break
            mi=(coordinates[0][1]-coordinates[i][1])/(coordinates[0][0]-coordinates[i][0])
            if mi!=m:
                ans=0
                break
        return ans