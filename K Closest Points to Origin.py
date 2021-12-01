#Submission 2 - 624ms 19.5mb
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda p:p[0]**2 + p[1]**2)
        return points[:k]

#Submission 1 - 5692ms 19.8mb
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d={}
        for p in points:
            dist=math.sqrt(p[0]**2 + p[1]**2)
            if dist in d:
                d[dist].append(p)
            else:
                d[dist]=[p]
        ans=[]
        while k:
            cur=min(d)
            ans+=d[cur]
            k-=len(d[cur])
            del d[cur]
        return ans