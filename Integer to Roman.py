class Solution:
    def intToRoman(self, num: int) -> str:
        roman=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        integer=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        ans=""
        for i in range(len(integer)):
            ans+=roman[i]*(num//integer[i])
            num=num%integer[i]
        return ans