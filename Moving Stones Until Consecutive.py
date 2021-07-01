#Submission 2 
class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        stones=[a,b,c]
        stones=sorted(stones)
        max_moves=stones[2]-stones[0]-2    #s[2]-s[1]-1+s[1]-s[0]-1
        if stones[2]-stones[1]==1 and stones[1]-stones[0]==1:
            return [0,max_moves]
        elif stones[2]-stones[1]<=2 or stones[1]-stones[0]<=2:
            return [1,max_moves]
        else:
            return [2,max_moves]

#Submission 1
class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        stones=[a,b,c]
        stones=sorted(stones)
        if stones[2]-stones[1]==1 and stones[1]-stones[0]==1:
            return [0,0]
        elif stones[2]-stones[1]<3 or stones[1]-stones[0]<3:
            return [1,stones[2]-stones[0]-2]
        else:
            return [2,stones[2]-stones[0]-2]