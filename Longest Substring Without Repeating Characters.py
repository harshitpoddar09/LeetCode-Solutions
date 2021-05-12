class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        queue=[]
        ans=0
        for i in s:
            while i in queue:
                queue.pop(0)
            else:
                queue.append(i)
            ans=max(ans,len(queue))
        return ans