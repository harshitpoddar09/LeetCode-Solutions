class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num[::-1])):
            if int(num[::-1][i])%2==1:
                return num[:len(num)-i]
        return ''