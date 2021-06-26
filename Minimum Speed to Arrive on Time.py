import math
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n=len(dist)
        if n-1>hour:
            return -1
        #low,mid,high are speeds
        low=1
        high=10**7+1
        while low<high:
            mid=low+(high-low)//2
            if dist[-1]/mid + sum(math.ceil(dist[i]/mid) for i in range(n-1)) <=hour:
                high=mid
            else:
                low=mid+1
        return low