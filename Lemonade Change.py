#Submission 2 - 144ms
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        b5=0
        b10=0
        for i in bills:
            if i==5:
                b5+=1
            elif i==10:
                b10+=1
                if b5:
                    b5-=1
                else:
                    return False
            else:
                if b5 and b10:
                    b5-=1
                    b10-=1
                elif b5>2:
                    b5-=3
                else:
                    return False
        return True

#Submission 1 - 1160ms
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cash=[]
        for i in bills:
            if i==5:
                cash.append(5)
            elif i==10:
                cash.append(10)
                if 5 in cash:
                    cash.remove(5)
                else:
                    return False
            else:
                cash.append(20)
                if 5 in cash and 10 in cash:
                    cash.remove(5)
                    cash.remove(10)
                elif cash.count(5)>=3:
                    cash.remove(5)
                    cash.remove(5)
                    cash.remove(5)
                else:
                    return False
        return True