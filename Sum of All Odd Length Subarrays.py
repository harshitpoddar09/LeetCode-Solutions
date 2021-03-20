class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans=sum(arr)
        k=len(arr)
        if len(arr)%2==0:
            k=len(arr)-1
        for i in range(1,(k//2)+1):
            for j in range(len(arr)-(2*i)):
                ans+=sum(arr[j:j+1+2*i])
        return ans