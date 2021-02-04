class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n=arr[len(arr)-1]
        missing=[]
        i=1
        while i<=n+k:
            if i not in arr:
                missing.append(i)
            i+=1
        return missing[k-1]