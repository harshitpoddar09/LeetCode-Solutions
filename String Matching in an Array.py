class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans=[]
        for i in range(len(words)):
            for j in words[:i]:
                if words[i] in j:
                    ans.append(words[i])
                    break
            else:
                for k in words[i+1:]:
                    if words[i] in k:
                        ans.append(words[i])
                        break
        return ans