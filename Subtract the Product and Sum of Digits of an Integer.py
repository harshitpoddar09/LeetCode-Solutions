class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod=1
        add=0
        for i in str(n):
            prod*=int(i)
            add+=int(i)
        return prod-add