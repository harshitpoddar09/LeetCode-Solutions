class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count=0
        heights_sort=sorted(heights)
        for i in range(len(heights)):
            if heights[i]!=heights_sort[i]:
                count+=1
        return count