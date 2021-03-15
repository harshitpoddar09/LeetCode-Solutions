"""
#Submission 2
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans=0
        for i in accounts:
            if sum(i)>ans:
                ans=sum(i)
        return ans
"""

#Submission 1
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        total=[]
        for i in accounts:
            total.append(sum(i))
        return max(total)
