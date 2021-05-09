class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        codes=[]
        for i in words:
            k=''
            for j in i:
                k+=morse[alphabets.index(j)]
            codes.append(k)
        return len(set(codes))