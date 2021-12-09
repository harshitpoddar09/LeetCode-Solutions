from collections import Counter
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        a=Counter(word1)
        b=Counter(word2)
        c=set(word1)
        d=set(word2)
        e=c.union(d)
        for ele in e:
            if ele in a:
                if ele in b:
                    if abs(a[ele]-b[ele])>3:
                        return False
                else:
                    if a[ele]>3:
                        return False
            else:
                if b[ele]>3:
                    return False
        return True