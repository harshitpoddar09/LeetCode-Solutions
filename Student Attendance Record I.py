class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A')>1:
            return 0
        for i in range(len(s)-2):
            if s[i]=='L':
                if s[i+1]=='L':
                    if s[i+2]=='L':
                        return 0
        return 1