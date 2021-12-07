class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort(reverse=True)
        n=len(arr)
        m=arr[n//2]
        arr.sort(key=lambda x:abs(x-m),reverse=True)
        return arr[:k]