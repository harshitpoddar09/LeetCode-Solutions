class Solution:
    def convertToBase7(self, num: int) -> str:
        ans=[]
        if num>0:
            while num!=0:
                ans.append(str(num%7))
                num=num//7
            ans.reverse()
            base_7=''.join(ans)
        elif num==0:
            base_7='0'
        else:
            num=abs(num)
            while num!=0:
                ans.append(str(num%7))
                num=num//7
            ans.reverse()
            base_7=''.join(ans)
            base_7= -1*int(base_7)
            base_7=str(base_7)
            
        return base_7