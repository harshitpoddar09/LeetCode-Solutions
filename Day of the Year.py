class Solution:
    def dayOfYear(self, date: str) -> int:
        year=int(date[0]+date[1]+date[2]+date[3])
        month=int(date[5]+date[6])
        Date=int(date[8]+date[9])
        if (year%4==0 and year%100!=0) or (year%400==0):
            feb=29
        else:
            feb=28
        days_months=[31,feb,31,30,31,30,31,31,30,31,30,31]
        if month==1:
            day=Date
        else:
            j=month-1
            day=0
            for i in range(j):
                day+=days_months[i]
            day+=Date
        return day