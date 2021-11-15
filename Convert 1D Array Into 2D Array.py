class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n!=len(original):
            return []
        ans=[]
        k=0
        for i in range(m):
            cur=[]
            for j in range(n):
                cur.append(original[k])
                k+=1
            ans.append(cur)
        return ans