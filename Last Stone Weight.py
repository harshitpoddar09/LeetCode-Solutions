class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=sorted(stones,reverse=True)
        while len(stones)>1:
            a=stones[0]-stones[1]
            stones.pop(0)
            stones.pop(0)
            i=0
            while stones and i<len(stones) and stones[i]>a:
                i+=1
            stones.insert(i,a)
        return stones[0]