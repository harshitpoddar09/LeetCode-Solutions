class Solution:
    def replaceDigits(self, s: str) -> str:
        alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for i in range(1,len(s),2):
            s=s.replace(s[i],alphabets[alphabets.index(s[i-1])+int(s[i])],1)
        return s