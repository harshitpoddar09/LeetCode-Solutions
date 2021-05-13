class Solution:
    def maximumTime(self, time: str) -> str:
        if time[0]=='?' and time[1]=='?':
            time=time.replace(time[0],'2',1)
            time=time.replace(time[1],'3',1)
        if time[0]=='?' and int(time[1])<=3:
            time=time.replace(time[0],'2',1)
        elif time[0]=='?' and int(time[1])>3:
            time=time.replace(time[0],'1',1)
        if time[1]=='?' and int(time[0])==2:
            time=time.replace(time[1],'3',1)
        elif time[1]=='?' and int(time[0])<2:
            time=time.replace(time[1],'9',1)
        if time[3]=='?':
            time=time.replace(time[3],'5',1)
        if time[4]=='?':
            time=time.replace(time[4],'9',1)
        return time