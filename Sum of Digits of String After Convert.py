class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num_s=''
        for i in s:
            num_s+=str(ord(i)-96)
        for j in range(k):
            new_s=sum(int(digit) for digit in num_s)
            num_s=str(new_s)
        return num_s