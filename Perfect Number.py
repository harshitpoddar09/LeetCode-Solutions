class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        add_div=1
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                add_div+=i+(num//i)
        if (int(num**0.5))**2==num:
            add_div-=int(num**0.5)
        return num==add_div