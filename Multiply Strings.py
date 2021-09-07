class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        d={}
        for i in range(10):
            for j in range(10):
                d[str(i)+str(j)]=i*j
        def prod(a,b):      #len(a)>len(b)
            ans=0
            b=b[::-1]
            p=0
            ans=0
            n=len(a)
            for i in b:
                q=n
                x=0
                for j in a:
                    x+=d[i+j]*(10**(q-1))
                    q-=1
                ans+=x*(10**p)
                p+=1
            return str(ans)
        if len(num1)>=len(num2):
            return prod(num1,num2)
        else:
            return prod(num2,num1)