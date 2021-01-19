class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle_min=minutes*6           # 1 min = 6 degree
        if hour==12:
            angle_hour=minutes*0.5    # 60 min of minute hand => 30 degree of hour hand
        else:
            angle_hour=hour*30+minutes*0.5
        angle=abs(angle_hour-angle_min)
        return min(angle,360-angle)
