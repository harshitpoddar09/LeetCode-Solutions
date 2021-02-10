class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=['a','e','i','o','u','A','E','I','O','U']
        s_vow=[]
        index=[]
        s_list=[]
        for i in range(len(s)):
            s_list.append(s[i])
            if s[i] in vowels:
                index.append(i)
                s_vow.append(s[i])
        s_vow.reverse()
        for j in range(len(index)):
            s_list[index[j]]=s_vow[j]
        return "".join(s_list)