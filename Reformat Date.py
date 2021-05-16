class Solution:
    def reformatDate(self, date: str) -> str:
        ans=date[-4:]+'-'
        months=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        for i in range(12):
            if months[i] in date:
                if i+1<10:
                    ans+='0'+str(i+1)+'-'
                else:
                    ans+=str(i+1)+'-'
        alphabets=['s','n','r','t']
        j=0
        temp=''
        while date[j] not in alphabets:
            temp+=date[j]
            j+=1
        if len(temp)==1:
            ans+='0'
        ans+=temp
        return ans