class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count=0
        total=sum(arr[0:k])
        if total//k>=threshold:
            count+=1
        for i in range(len(arr)-k):
            total=total-arr[i]+arr[i+k]
            if total//k>=threshold:
                count+=1
        return count