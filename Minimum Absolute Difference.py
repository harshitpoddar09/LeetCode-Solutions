#Submission 2 - 492ms
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans=[]
        min_diff=arr[1]-arr[0]
        for i in range(1,len(arr)):
            min_diff=min(min_diff,arr[i]-arr[i-1])
        for i in range(1,len(arr)):
            if arr[i]-arr[i-1]==min_diff:
                ans.append([arr[i-1],arr[i]])
        return ans

#Submission 1 - 608ms
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans=[]
        cur_diff=arr[1]-arr[0]
        min_diff=cur_diff
        for i in range(1,len(arr)):
            cur_diff=arr[i]-arr[i-1]
            if cur_diff==min_diff:
                ans.append([arr[i-1],arr[i]])
            elif cur_diff<min_diff:
                min_diff=cur_diff
                ans=[[arr[i-1],arr[i]]]
        return ans