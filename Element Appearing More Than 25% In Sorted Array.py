class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        for i in arr:
            if arr.count(i)>len(arr)//4:
                return i