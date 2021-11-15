#SUBMISSION 2 - 102ms
class Solution:
    def minOperations(self, n: int) -> int:
        end=(2*(n-1))+1
        initial=(end-1)//2
        ans=0
        for i in range(n//2):
            ans+=initial
            initial-=2
        return ans

#SUBMISSION 1 - 162ms 
class Solution:
    def minOperations(self, n: int) -> int:
        start=1
        end=(2*(n-1))+1
        ans=0
        while start<end:
            ans+=(end-start)//2
            start+=2
            end-=2
        return ans