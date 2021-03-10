class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count=0
        for i in items:
            if (ruleKey=='type' and ruleValue==i[0]) or (ruleKey=='color' and ruleValue==i[1]) or (ruleKey=='name' and ruleValue==i[2]):
                count+=1
        return count