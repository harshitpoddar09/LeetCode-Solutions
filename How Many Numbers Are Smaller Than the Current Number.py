class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            count=0
            for j in sorted(nums[0:i]):
                if j<nums[i]:
                    count+=1
                else:
                    break
            for k in sorted(nums[i+1:]):
                if k<nums[i]:
                    count+=1
                else:
                    break
            ans.append(count)
        return ans