class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        i=1
        while i<len(ranges):
            if ranges[i][0]<=ranges[i-1][1]:
                ranges[i-1][1]=max(ranges[i-1][1],ranges[i][1])
                ranges.pop(i)
            else:
                i+=1
        if left>ranges[-1][1] or right>ranges[-1][1]:
            return False
        need=[i for i in range(right,left-1,-1)]
        i=0
        n=len(ranges)
        while i<n:
            if ranges[i][0]<=left and ranges[i][1]>=left:
                if right<=ranges[i][1]:
                    return True
                else:
                    while right>ranges[i][1]:
                        i+=1
                        if ranges[i][0]-1!=ranges[i-1][1]:
                            return False
                    return True
            i+=1