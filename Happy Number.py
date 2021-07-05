#Submission 2 - 36 ms
class Solution:
    def isHappy(self, n: int) -> bool:
        d={}
        while n!=1:
            a=0
            for i in str(n):
                a+=int(i)**2
            n=a
            if n in d:
                return 0
            else:
                d[n]=1
        return 1
        
#Submission 1 - 32 ms
class Solution:
    def isHappy(self, n: int) -> bool:
        d={}
        if n==1:
            return 1
        while True:
            a=0
            for i in str(n):
                a+=int(i)**2
            n=a
            if n==1:
                return 1
            elif n in d:
                return 0
            else:
                d[n]=1
        return 1
