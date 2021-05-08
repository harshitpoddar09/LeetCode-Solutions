#Submission2 - 28ms
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('U')==moves.count('D') and moves.count('R')==moves.count('L')

#Submission1 - 56ms
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x=0
        y=0
        for i in moves:
            if i=='U':
                y+=1
            elif i=='D':
                y-=1
            elif i=='R':
                x+=1
            else:
                x-=1
        if x==0 and y==0:
            return 1
        return 0