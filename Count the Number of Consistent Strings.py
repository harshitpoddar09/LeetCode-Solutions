class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        for j in words:
            for i in j:
                if i not in allowed:
                    break
            else:
                count+=1
        return count