#Submission 2- 80ms
class Solution:
    def maxPower(self, s: str) -> int:
        prev='0'
        count=1
        ans=1
        for i in s:
            if prev==i:
                count+=1
            else:
                prev=i
                count=1
            ans=max(ans,count)
        return ans
        
#Submission 1- 56ms
class Solution:
    def maxPower(self, s: str) -> int:
        queue=[s[0]]
        i=1
        ans=1
        while i<len(s):
            if queue[-1]==s[i]:
                queue.append(s[i])
            else:
                ans=max(ans,len(queue))
                queue=[s[i]]
            i+=1
        ans=max(ans,len(queue))
        return ans