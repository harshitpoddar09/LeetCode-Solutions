class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        arr=[[profits[i],capital[i]] for i in range(len(capital))]
        ans=w
        arr.sort(key=lambda x:x[1])
        arr.sort(key=lambda x:x[0],reverse=True)
        i=0
        a=min(k,len(arr))
        while i<a:
            j=0
            while j<len(arr) and ans<arr[j][1]:
                j+=1
            if j==len(arr):
                return ans
            ans+=arr[j][0]
            arr.pop(j)
            i+=1
        return ans