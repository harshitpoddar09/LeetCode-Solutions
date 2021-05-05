class Solution:
    def romanToInt(self, s: str) -> int:
        roman_1=['CM','CD','XC','XL','IX','IV']
        roman_2=['M','D','C','L','X','V','I']
        integer_1=[900,400,90,40,9,4]
        integer_2=[1000,500,100,50,10,5,1]
        ans=0
        for i in range(6):
            if roman_1[i] in s:
                ans+=integer_1[i]
                s=s.replace(roman_1[i],'')
        for j in s:
            ans+=integer_2[roman_2.index(j)]
            s=s.replace(j,'',1)
        return ans