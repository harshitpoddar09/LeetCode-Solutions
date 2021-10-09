class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for word in strs:
            key=''.join(sorted(word))
            if key in d:
                d[key].append(word)
            else:
                d[key]=[word]
        ans=[]
        for key in d:
            ans.append(d[key])
        return ans