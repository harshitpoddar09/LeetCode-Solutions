class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans=[]
        a=nums[:n]
        b=nums[n:]
        for i in range(n):
            ans.append(a[i])
            ans.append(b[i])
        return ans