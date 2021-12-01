from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d=Counter(words)
        new={}
        for key in d:
            freq=d[key]
            if freq not in new:
                new[freq]=[]
            new[freq].append(key)
        ans=[]
        while k:
            max_freq=max(new)
            new[max_freq].sort()
            ans.append(new[max_freq][0])
            new[max_freq].pop(0)
            if len(new[max_freq])==0:
                del new[max_freq]
            k-=1
        return ans