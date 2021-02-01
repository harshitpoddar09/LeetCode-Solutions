class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start=[]
        end=[]
        for i in range(len(paths)):
            start.append(paths[i][0])
            end.append(paths[i][1])
        for j in end:
            if j not in start:
                return j