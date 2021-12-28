class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        arr_min=[]
        arr_max=[]
        lo=float('-inf')
        hi=float('inf')
        ans=0
        for i in nums:
            arr_min.append(lo)
            lo=max(lo,i)
        for j in range(len(nums)-1,-1,-1):
            arr_max.append(hi)
            hi=min(hi,nums[j])
        arr_max.reverse()
        for k in range(1,len(nums)-1):
            if arr_min[k]<nums[k]<arr_max[k]:
                ans+=2
            elif nums[k-1]<nums[k]<nums[k+1]:
                ans+=1
        return ans