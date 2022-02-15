#Submission 4 - 247 ms 16.7 mb
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for i in nums:
            xor = xor^i
        return xor

#Submission 3 - 168 ms 17.1 mb
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        for i in nums:
            if i in s:
                s.remove(i)
            else:
                s.add(i)
        for i in s:
            return i

#Submission 2 - 162 ms 16.6 mb
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = Counter(nums)
        for key in d:
            if d[key] == 1:
                return key

#Submission 1 - 5700 ms 16.5 mb
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i)==1:
                return i
