from collections import Counter
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        freq=Counter(groupSizes)
        d={}
        ans=[]
        for idx in range(len(groupSizes)):
            size=groupSizes[idx]
            if size not in d:
                d[size]=[idx]
                if size==1:
                    ans.append(d[size])
                    d[size]=[]
            else:
                d[size].append(idx)
                if len(d[size])==size:
                    ans.append(d[size])
                    d[size]=[]
        return ans