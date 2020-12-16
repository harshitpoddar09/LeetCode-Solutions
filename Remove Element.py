class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a=nums.count(val)
        for i in range(a):
            nums.remove(val)
        return len(nums)