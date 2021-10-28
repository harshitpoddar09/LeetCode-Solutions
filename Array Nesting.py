class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        ans=1
        visited=[False for i in range(len(nums))]
        for i in range(len(nums)):
            idx=i
            if not visited[i]:
                cur=set()
                while nums[idx] not in cur:
                    cur.add(nums[idx])
                    visited[idx]=True
                    idx=nums[idx]
                ans=max(ans,len(cur))
        return ans