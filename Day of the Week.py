import calendar
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        day_num=calendar.weekday(year,month,day)
        days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        return days[day_num]