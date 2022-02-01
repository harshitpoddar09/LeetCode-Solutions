class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n=len(arr)
        if n<2:
            return 0
        d={}
        for idx,val in enumerate(arr):
            if val not in d:
                d[val]=[]
            d[val].append(idx)
        cur=[0]
        visited={0}
        ans=0
        while cur:
            temp=[]
            for idx in cur:
                if idx==n-1:
                    return ans
                for i in d[arr[idx]]:
                    if i not in visited:
                        visited.add(i)
                        temp.append(i)
                d[arr[idx]].clear()
                for i in [idx-1,idx+1]:
                    if i>-1 and i<n and i not in visited:
                        visited.add(i)
                        temp.append(i)
            cur=temp
            ans+=1
        return -1