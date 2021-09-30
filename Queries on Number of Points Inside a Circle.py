class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans=[]
        for i in queries:
            num=0
            for j in points:
                if ((j[0]-i[0])**2)+((j[1]-i[1])**2)<=i[2]**2:
                    num+=1
            ans.append(num)
        return ans