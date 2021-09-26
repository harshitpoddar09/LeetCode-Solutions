class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_row = {min(r) for r in matrix}
        max_col = {max(c) for c in zip(*matrix)} 
        ans=[]
        for i in min_row:
            if i in max_col:
                ans.append(i)
        return ans