#Submission 2 - 220ms 25.7mb
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        nums[:]=nums[-k:]+nums[:-k]

#Submission 1 - 3108ms 25.9mb
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k%len(nums)):
            nums.insert(0,nums[-1])
            nums.pop()
