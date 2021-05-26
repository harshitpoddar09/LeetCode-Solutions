#Submission2 - 700ms, 19.2mb
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ans=-1
        distance=10**5
        for i in range(len(points)):
            if (points[i][0]==x or points[i][1]==y) and distance>abs(x-points[i][0])+abs(y-points[i][1]):
                ans=i
                distance=abs(x-points[i][0])+abs(y-points[i][1])
        return ans

#Submission1 - 768ms, 19.4mb
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        same=[]
        for i in range(len(points)):
            if points[i][0]==x or points[i][1]==y:
                same.append(points[i])
        if len(same)==0:
            return -1
        distance=[]
        for j in same:
            distance.append(abs(x-j[0])+abs(y-j[1]))
        ind=distance.index(min(distance))
        return points.index(same[ind])