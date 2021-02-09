class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new_arr=[]
        for i in arr:
            new_arr.append(i)
        for j in range(len(arr)-1):
            new_arr.pop(0)
            maximum=max(new_arr)
            arr[j]=maximum
        arr[len(arr)-1]=-1
        return arr