class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        idx=[]
        for i in range(len(s)):
            if s[i]==c:
                idx.append(i)
        j=0
        ans=[]
        for k in range(len(s)):
            if k>idx[j] and j<len(idx)-1:
                j+=1
            if j>0:
                ans.append(min(abs(idx[j]-k),abs(idx[j-1]-k)))
            else:
                ans.append(abs(idx[0]-k))
        return ans