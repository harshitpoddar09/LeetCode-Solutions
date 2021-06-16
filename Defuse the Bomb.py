class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k==0:
            return [0]*len(code)
        ans=[]
        n=len(code)
        code+=code
        if k>0:
            for i in range(n):
                ans.append(sum(code[i+1:i+1+k]))
            return ans
        for i in range(n,2*n):
            ans.append(sum(code[i-1:i-1+k:-1]))
        return ans