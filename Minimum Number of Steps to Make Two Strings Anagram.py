from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        a=Counter(s)
        b=Counter(t)
        ans=0
        for key in a:
            if key not in b:
                ans+=a[key]
            elif a[key]>b[key]:
                ans+=a[key]-b[key]
        return ans