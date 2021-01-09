class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        ar=[]
        for i in arr:
            ar.append(i)
        j=1
        for i in range(len(ar)):
            if ar[i]==0:
                arr.insert(i+j,0)
                arr.pop()
                j+=1