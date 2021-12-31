class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points=[p1,p2,p3,p4]
        points.sort(key=lambda x:x[0])
        points.sort(key=lambda x:x[1])
        temp=points[2]
        points[2]=points[3]
        points[3]=temp
        def distance(a,b):
            d=((a[0]-b[0])**2) + ((a[1]-b[1])**2)
            return d
        dist=distance(points[0],points[3])
        for i in range(3):
            a=distance(points[i],points[i+1])
            if a!=dist:
                return False
        return distance(points[0],points[2])==distance(points[1],points[3]) and dist!=0