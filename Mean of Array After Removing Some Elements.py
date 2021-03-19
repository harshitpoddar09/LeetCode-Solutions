class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n=(5*len(arr))//100
        arr=arr[n:len(arr)-n]
        return sum(arr)/len(arr)