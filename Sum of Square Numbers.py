import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(math.sqrt(c))+1):
            b=math.sqrt(c-(a*a))
            if b==int(b):
                return True
        return False