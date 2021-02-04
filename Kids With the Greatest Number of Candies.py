class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        original_max=max(candies)
        ans=[]
        for i in candies:
            ans.append(i+extraCandies>=original_max)
        return ans