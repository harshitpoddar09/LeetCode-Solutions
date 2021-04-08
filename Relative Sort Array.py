class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans=[]
        for i in arr2:
            for j in range(arr1.count(i)):
                ans.append(i)
                arr1.remove(i)
        arr1.sort()
        return ans+arr1