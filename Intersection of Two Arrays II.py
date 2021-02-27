class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1=len(nums1)
        n2=len(nums2)
        intersection=[]
        if n1<n2:
            for i in set(nums1):
                for j in range(min(nums1.count(i),nums2.count(i))):
                    intersection.append(i)
        else:
            for i in set(nums2):
                for j in range(min(nums1.count(i),nums2.count(i))):
                    intersection.append(i)
        return intersection