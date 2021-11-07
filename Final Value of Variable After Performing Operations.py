class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans=0
        for i in operations:
            if i=='X++' or i=='++X':
                ans+=1
            else:
                ans-=1
        return ans