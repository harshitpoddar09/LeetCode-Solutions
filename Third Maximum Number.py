class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        count_list={}
        for p in nums:
            count_list[p]=nums.count(p)
        value_list=list(count_list.values())
        if len(value_list)>2:
            a=nums.count(max(nums))
            for i in range(a):
                nums.remove(max(nums))
            b=nums.count(max(nums))
            for j in range(b):
                nums.remove(max(nums))
            return max(nums)
        else:
            return max(nums)