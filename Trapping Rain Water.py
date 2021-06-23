class Solution:
    def trap(self, height: List[int]) -> int:
        ans=0
        for i in range(1,len(height)-1):
            ans+=max(min(max(height[:i]),max(height[i+1:]))-height[i],0)
        return ans