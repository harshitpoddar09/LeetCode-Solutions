class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        i=0
        while i<len(arr)-2 and arr[i+1]>arr[i]:
            i+=1
        if i==0:
            return False
        while i<len(arr)-1 and arr[i+1]<arr[i]:
            i+=1
        if i==len(arr)-1:
            return True
        return False