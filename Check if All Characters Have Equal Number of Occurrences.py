from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        new=Counter(s)
        count=new[s[0]]
        for key in new:
            if new[key]!=count:
                return False
        return True