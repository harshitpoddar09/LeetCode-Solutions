#Submission 2 - 20ms
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        ans=''
        for i in title.split():
            i=i.lower()
            if len(i)>2:
                ans+=i.capitalize()+' '
            else:
                ans+=i+' '
        return ans[:-1]

#Submission 1 - 59ms
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title=title.lower()
        ans=''
        for i in title.split():
            if len(i)>2:
                ans+=i.capitalize()+' '
            else:
                ans+=i+' '
        return ans[:-1]