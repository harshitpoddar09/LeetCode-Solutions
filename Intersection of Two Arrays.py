class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sets1=set(nums1)
        sets2=set(nums2)
        ans=[]
        for i in sets1:
            if i in sets2:
                ans.append(i)
        return ans