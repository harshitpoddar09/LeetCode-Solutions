class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        queue=[s[0]]
        flag=s[0]
        i=1
        ans=0
        while i<len(s):
            if s[i]==queue[-1]:
                while i<len(s) and queue[-1]==s[i]:
                    queue.append(s[i])
                    i+=1
            else:
                flag=s[i]
                a=len(queue)
                b=0
                while i<len(s) and s[i]==flag:
                    queue.append(s[i])
                    b+=1
                    i+=1
                ans+=min(a,b)
                queue=queue[a:]
        return ans