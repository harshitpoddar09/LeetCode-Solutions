from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        a=Counter(s)
        ans=''
        for i in range(len(a)):
            key=max(a,key=lambda x:a[x])
            ans+=key*a[key]
            del a[key]
        return ans