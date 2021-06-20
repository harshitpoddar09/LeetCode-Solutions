class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        ans=A[0]
        for i in ans:
            for j in range(1,len(A)):
                if i not in A[j]:
                    ans=ans.replace(i,'',1)
                    break
                else:
                    A[j]=A[j].replace(i,'',1)
        return ans