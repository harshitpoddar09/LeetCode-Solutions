class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if '10' in s and '01' in s:
            return False
        return True