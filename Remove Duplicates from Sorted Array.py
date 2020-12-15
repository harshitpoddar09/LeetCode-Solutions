class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #Submission 1
        for i in nums:
            n=nums.count(i)
            for j in range(n-1):
                nums.remove(i)
        return len(nums)
        
        #Submission 2
        for i in nums:
            while nums.count(i)>1:
                nums.remove(i)
        return len(nums)