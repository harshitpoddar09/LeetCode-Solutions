class Solution:
    def isThree(self, n: int) -> bool:
        div=2
        for i in range(2,n):
            if n%i==0:
                div+=1
            if div>3:
                return False
        return div==3