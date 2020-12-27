class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        sq_rt=num**0.5
        return sq_rt.is_integer()