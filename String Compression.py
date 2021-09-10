#Submission 2 - 60ms
class Solution:
    def compress(self, chars: List[str]) -> int:
        i=0
        s=''
        count=1
        while i<len(chars):
            if i>0 and chars[i]==chars[i-1]:
                count+=1
            else:
                if count!=1:
                    s+=str(count)
                s+=chars[i]
                count=1
            i+=1
        if count>1:
            s+=str(count)
        chars.clear()
        chars+=list(s)
        return len(chars)

#Submission 1 - 64ms
class Solution:
    def compress(self, chars: List[str]) -> int:
        i=0
        s=''
        count=1
        n=len(chars)
        while i<len(chars):
            if i>0 and chars[i]==chars[i-1]:
                count+=1
            else:
                if count!=1:
                    s+=str(count)
                s+=chars[i]
                count=1
            i+=1
        if count>1:
            s+=str(count)
        for i in s[::-1]:
            chars.insert(0,i)
        chars=chars[:-n]
        return len(chars)