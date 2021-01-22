class Solution:
    def bulbSwitch(self, n: int) -> int:
        #When I tried writing solving for n=1 to n=9, I realised the ans is always the integer part of square root of n
        return int(sqrt(n))

        
        #Method1 but exceeds time limit
        """
        if n==0:
            ans=0
        elif n==1:
            ans=1
        else:
            bulbs=[1 for i in range(n)]
            for j in range(2,n+1):
                for k in range(len(bulbs)):
                    if (k+1)%j==0:
                        if bulbs[k]==1:
                            bulbs[k]=0
                        else:
                            bulbs[k]=1
            ans=0
            for m in bulbs:
                if m==1:
                    ans+=1
        return ans
        """