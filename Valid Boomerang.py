#Submission 2 - 20ms 
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        m1=(points[1][1]-points[0][1])*(points[2][0]-points[0][0])
        m2=(points[2][1]-points[0][1])*(points[1][0]-points[0][0])
        return m1!=m2

#Submission 1 - 36ms
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        if points[0]==points[1] or points[1]==points[2] or points[2]==points[0]:
            return False
        if points[0][0]==points[1][0] and points[0][0]==points[2][0]:
            return False
        elif points[0][0]==points[1][0] or points[0][0]==points[2][0] or points[1][0]==points[2][0]:
            return True
        m1=(points[1][1]-points[0][1])/(points[1][0]-points[0][0])
        m2=(points[2][1]-points[0][1])/(points[2][0]-points[0][0])
        return m1!=m2