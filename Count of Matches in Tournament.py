class Solution:
    def numberOfMatches(self, n: int) -> int:
        num=0
        while n>1:
            num_round=n//2
            num+=num_round
            if n%2==0:
                n = n//2
            else:
                n = n//2 + 1
        return num