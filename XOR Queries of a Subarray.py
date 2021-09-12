class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix=[0]
        for i in arr:
            prefix.append(prefix[-1]^i)
        ans=[]
        for j in queries:
            ans.append(prefix[j[1]+1]^prefix[j[0]])
        return ans