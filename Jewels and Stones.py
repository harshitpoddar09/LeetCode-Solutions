#Submission 2 - 32 ms
from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans=0
        jewels=set(jewels)
        for i in stones:
            if i in jewels:
                ans+=1
        return ans

#Submission 1 - 32 ms
from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans=0
        stones=Counter(stones)
        for i in jewels:
            if i in stones:
                ans+=stones[i]
        return ans