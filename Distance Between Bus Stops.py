class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        a=min(start,destination)
        b=max(start,destination)
        dis_clk=0
        for i in range(a,b):
            dis_clk+=distance[i]
        dis_aclk=0
        for j in range(0,a):
            dis_aclk+=distance[j]
        for k in range(b,len(distance)):
            dis_aclk+=distance[k]
        ans=min(dis_clk,dis_aclk)
        if ans==0:
            dmin=max(dis_clk,dis_aclk)
        else:
            dmin=ans
        return dmin