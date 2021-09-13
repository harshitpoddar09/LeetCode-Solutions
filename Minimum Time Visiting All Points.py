class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans=0
        cur_x=points[0][0]
        cur_y=points[0][1]
        points.pop(0)
        for x,y in points:
            ans+=max(abs(x-cur_x),abs(y-cur_y))
            cur_x=x
            cur_y=y
        return ans