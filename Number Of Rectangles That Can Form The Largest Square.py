class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        square=[]
        for i in rectangles:
            square.append(min(i))
        return square.count(max(square))