#Submission 2 - 28ms
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s=s.split()
        nums=[]
        for i in s:
            if i.isnumeric():
                nums.append(int(i))
                if len(nums)>1:
                    if nums[-1]<=nums[-2]:
                        return False
        return True

#Submission 1 - 54ms
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s=s.split()
        nums=[]
        for i in s:
            if i.isnumeric():
                nums.append(int(i))
                if len(nums)>1:
                    if nums[-1]==nums[-2]:
                        return False
        return nums==sorted(nums)