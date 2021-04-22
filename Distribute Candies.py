class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        a=len(set(candyType))
        return min(len(candyType)//2,a)