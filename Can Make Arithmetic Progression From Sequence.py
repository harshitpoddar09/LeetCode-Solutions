class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        d=arr[1]-arr[0]
        count=0
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]==d:
                count+=1
        return count==len(arr)-1