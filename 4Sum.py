class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                left=j+1
                right=len(nums)-1
                while left<right:
                    a=nums[i]+nums[j]+nums[left]+nums[right]
                    if a==target:
                        ans.append([nums[i],nums[j],nums[left],nums[right]])
                        left+=1
                        right-=1
                        while left<right and nums[left]==nums[left-1]:
                            left+=1
                        while left<right and nums[right]==nums[right+1]:
                            right-=1
                    elif a<target:
                        left+=1
                    else:
                        right-=1
        return ans