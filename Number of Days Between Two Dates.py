from datetime import date
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        y1=int(date1[:4])
        m1=int(date1[5:7])
        d1=int(date1[8:])
        y2=int(date2[:4])
        m2=int(date2[5:7])
        d2=int(date2[8:])
        day1=date(y1,m1,d1)
        day2=date(y2,m2,d2)
        return abs((day2-day1).days)