#Submission 2 - 1930ms
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        ans=0
        end=-float('inf')
        for x,y in points:
            if x>end:
                ans+=1
                end=y
        return ans

#Submission 1 - 2636ms
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        ans=0
        end=-float('inf')
        for i in points:
            if i[0]>end:
                ans+=1
                end=i[1]
        return ans