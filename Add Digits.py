class Solution:
    def addDigits(self, num: int) -> int:
        sum=100
        while sum%10!=sum:
            sum=0
            for i in str(num):
                sum+=int(i)
            num=sum
            if sum%10==sum:
                return sum