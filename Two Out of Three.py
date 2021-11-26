class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1=set(nums1)
        nums2=set(nums2)
        nums3=set(nums3)
        a=nums1.intersection(nums2)
        b=nums2.intersection(nums3)
        c=nums3.intersection(nums1)
        d=a.union(b,c)
        return list(d)