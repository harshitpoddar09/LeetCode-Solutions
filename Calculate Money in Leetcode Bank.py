class Solution:
    def totalMoney(self, n: int) -> int:
        num_weeks=n//7
        remaining_days=n%7
        if num_weeks<1:
            amount=(n*(n+1))//2   #sum of first n natural numbers
        else:
            extra=0
            for i in range(1,remaining_days+1):
                extra+=num_weeks+i
            week1=28     #1+2+3+4+5+6+7
            weekly=0
            for j in range(1,num_weeks+1):
                weekly+=week1+7*(j-1)
            amount=weekly+extra
        return amount