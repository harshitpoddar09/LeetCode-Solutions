class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans=9999999
        nums=sorted(nums)
        n=len(nums)
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=n-1
            while l<r:
                a=nums[i]+nums[l]+nums[r]
                if a==target:
                    return target
                else:
                    if abs(ans-target)>abs(a-target):
                        ans=a
                    if a>target:
                        r-=1
                    else:
                        l+=1
        return ans