class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s=s.lower()
        vowels=['a','e','i','o','u']
        count1=0
        count2=0
        for i in s[:len(s)//2]:
            if i in vowels:
                count1+=1
        for j in s[len(s)//2:]:
            if j in vowels:
                count2+=1
        return count1==count2