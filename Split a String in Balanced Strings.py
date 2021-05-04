class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count_l=0
        count_r=0
        ans=0
        for i in range(len(s)):
            if s[i]=='L':
                count_l+=1
            else:
                count_r+=1
            if count_l==count_r:
                ans+=1
        return ans