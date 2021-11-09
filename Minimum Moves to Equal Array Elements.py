class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # sum(nums)+(m*(n-1))=x*n
        # x = final value of all elements
        # m=min no of moves
        return sum(nums)-(len(nums)*min(nums))