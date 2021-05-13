class Solution:
    def reformatNumber(self, number: str) -> str:
        number=number.replace(' ','')
        number=number.replace('-','')
        ans=''
        while len(number)>0:
            if len(number)>4:
                ans+=number[:3]+'-'
                number=number[3:]
            elif len(number)==4:
                ans+=number[:2]+'-'+number[2:]
                number=''
            elif len(number)<=3:
                ans+=number
                number=''
        return ans