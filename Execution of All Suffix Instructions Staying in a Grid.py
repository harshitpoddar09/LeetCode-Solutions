class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        def check(x,y,n):
            if x>-1 and x<n and y>-1 and y<n:
                return True
            else:
                return False
        ans=[0]*len(s)
        for i in range(len(s)):
            x=startPos[0]
            y=startPos[1]
            cur=0
            for j in range(i,len(s)):
                if s[j]=='R':
                    y+=1
                elif s[j]=='L':
                    y-=1
                elif s[j]=='U':
                    x-=1
                else:
                    x+=1
                if check(x,y,n):
                    cur+=1
                else:
                    break
            ans[i]=cur
        return ans