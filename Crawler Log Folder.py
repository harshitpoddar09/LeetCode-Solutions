class Solution:
    def minOperations(self, logs: List[str]) -> int:
        main=0
        for i in logs:
            if i=='./':
                continue
            elif i=='../':
                main=max(0,main-1)
            else:
                main+=1
        return main