class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels=['a','e','i','o','u','A','E','I','O','U']
        words=list(S.split())
        for i in range(len(words)):
            if words[i][0] in vowels:
                words[i]+='ma'
            else:
                words[i]+=words[i][0]
                words[i]=words[i].replace(words[i][0],'',1)
                words[i]+='ma'
            words[i]+='a'*(i+1)
        return ' '.join(words)