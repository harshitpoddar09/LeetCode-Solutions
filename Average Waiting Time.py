class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n=len(customers)
        t1=customers[0][1]
        time=[t1]
        t_start=customers[0][0]
        t_end=t_start+t1
        for i in range(1,n):
            if t_end>customers[i][0]:
                ti=t_end-customers[i][0]
                t_end+=customers[i][1]
            else:
                ti=0
                t_end=customers[i][0]+customers[i][1]
            ti+=customers[i][1]
            time.append(ti)
        return (sum(time))/n