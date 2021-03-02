class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for i in nums1:
            j=nums2.index(i)
            ans.append(-1)
            while j<len(nums2):
                if nums2[j]>i:
                    ans.pop()
                    ans.append(nums2[j])
                    break
                else:
                    j+=1
        return ans