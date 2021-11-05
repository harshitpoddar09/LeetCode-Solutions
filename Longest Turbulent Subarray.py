class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                arr[i]=1
            elif arr[i]<arr[i+1]:
                arr[i]=-1
            else:
                arr[i]=0
        arr.pop()
        ans=0
        i=0
        flag=0
        check=0
        cur=0
        while i<len(arr):
            if check==0:
                if arr[i]==1:
                    flag=True
                    cur=1
                    check=1
                elif arr[i]==-1:
                    flag=False
                    cur=1
                    check=1
                i+=1
            else:
                if flag:
                    if arr[i]==-1:
                        cur+=1
                        flag=False
                        i+=1
                    else:
                        check=0
                else:
                    if arr[i]==1:
                        cur+=1
                        flag=True
                        i+=1
                    else:
                        check=0
            ans=max(ans,cur)
        return ans+1