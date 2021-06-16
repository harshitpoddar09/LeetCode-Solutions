#Submission2: 52ms
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        ans=keysPressed[0]
        duration=releaseTimes[0]
        for i in range(len(releaseTimes)-1):
            if duration<releaseTimes[i+1]-releaseTimes[i]:
                ans=keysPressed[i+1]
                duration=releaseTimes[i+1]-releaseTimes[i]
            elif duration==releaseTimes[i+1]-releaseTimes[i] and keysPressed[i+1]>ans:
                ans=keysPressed[i+1]
        return ans
        
#Submission1: 188ms
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        for i in range(len(releaseTimes)-1,0,-1):
            releaseTimes[i]-=releaseTimes[i-1]
        idx=[]
        for j in range(len(releaseTimes)):
            if releaseTimes[j]==max(releaseTimes):
                idx.append(j)
        keys=[keysPressed[k] for k in idx]
        return sorted(keys)[-1]