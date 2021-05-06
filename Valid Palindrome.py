#Submission 2: 40ms
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        word=''
        for i in s:
            if i.isalnum():
                word+=i
        if word==word[::-1]:
            return True
        else:
            return False
            
#Submission 1 : 1244ms
class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in s:
            if not i.isalnum():
                s=s.replace(i,'')
        if s.lower()==(s.lower())[::-1]:
            return True
        else:
            return False