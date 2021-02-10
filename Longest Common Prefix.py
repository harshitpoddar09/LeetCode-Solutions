class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=''
        length=[]
        if len(strs)>0:
            for i in range(len(strs)):
                length.append(len(strs[i]))
            for j in range(min(length)):
                for k in range(1,len(strs)):
                    if strs[k][j]!=strs[0][j]:
                        return ans
                else:
                    ans+=strs[0][j]
        return ans   