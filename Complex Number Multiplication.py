class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        r1=''
        j=0
        while j<len(num1) and num1[j]!='+':
            r1+=num1[j]
            j+=1
        j+=1
        i1=num1[j:len(num1)-1]
        r2=''
        k=0
        while k<len(num2) and num2[k]!='+':
            r2+=num2[k]
            k+=1
        k+=1
        i2=num2[k:len(num2)-1]
        r1=int(r1)
        i1=int(i1)
        r2=int(r2)
        i2=int(i2)
        r=(r1*r2)-(i1*i2)
        i=(r1*i2)+(r2*i1)
        return str(r)+'+'+str(i)+'i'