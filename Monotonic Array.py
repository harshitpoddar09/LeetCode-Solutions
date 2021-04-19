class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if A==sorted(A) or A==sorted(A,reverse=True):
            return 1
        return 0