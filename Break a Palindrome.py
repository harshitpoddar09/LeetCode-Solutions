class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome)==1:
            return ''
        for i in range(len(palindrome)//2):
            char=palindrome[i]
            if char!='a':
                palindrome=palindrome.replace(char,'a',1)
                return palindrome
        palindrome=list(palindrome)
        palindrome[-1]='b'
        return ''.join(palindrome)