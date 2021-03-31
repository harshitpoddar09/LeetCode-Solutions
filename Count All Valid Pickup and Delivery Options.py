class Solution:
    def countOrders(self, n: int) -> int:
        prod=1
        for i in range(2,n*2+1):
            prod*=i
        return (prod//(2**n))%(10**9+7)