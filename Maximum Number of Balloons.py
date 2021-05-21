#Submission 1 - 48 ms
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ans=0
        while len(text)>0:
            for i in 'balloon':
                if i in text:
                    text=text.replace(i,'',1)
                else:
                    return ans
            ans+=1
        return ans
        
#Submission 2 - 32 ms
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        return min(text.count('b'),text.count('a'),text.count('l')//2,text.count('o')//2,text.count('n'))