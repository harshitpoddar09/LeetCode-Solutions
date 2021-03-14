class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        total=[]
        for i in accounts:
            total.append(sum(i))
        return max(total)