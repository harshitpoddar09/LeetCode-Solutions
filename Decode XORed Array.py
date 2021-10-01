class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans=[first]
        cur=first
        for i in encoded:
            cur=cur^i
            ans.append(cur)
        return ans