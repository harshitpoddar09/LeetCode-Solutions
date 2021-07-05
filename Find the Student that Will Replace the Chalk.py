class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        i=0
        k=k%sum(chalk)
        while k>=chalk[i]:
            k-=chalk[i]
            if i+1<len(chalk):
                i+=1
            else:
                i=0
        return i