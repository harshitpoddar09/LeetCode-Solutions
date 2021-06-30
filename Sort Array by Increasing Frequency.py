from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freqDict=Counter(nums)
        counts=freqDict.items()
        counts=sorted(counts,reverse=True)
        counts=sorted(counts, key=lambda x:x[1])
        ans=[]
        for i in counts:
            ans+=[i[0]]*i[1]
        return ans