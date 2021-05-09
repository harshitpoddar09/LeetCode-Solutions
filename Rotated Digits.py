class Solution:
    def rotatedDigits(self, N: int) -> int:
        ans=0
        for i in range(1,N+1):
            j=''
            a=str(i)
            for k in range(len(a)):
                if a[k]=='3' or a[k]=='4' or a[k]=='7':
                    break
                elif a[k]=='5':
                    j+='2'
                elif a[k]=='2':
                    j+='5'
                elif a[k]=='6':
                    j+='9'
                elif a[k]=='9':
                    j+='6'
                else:
                    j+=a[k]
            if len(j)==len(a) and j!=a:
                ans+=1
        return ans