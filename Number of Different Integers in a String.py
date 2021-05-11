class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for i in word:
            if i in alphabets:
                word=word.replace(i,' ',1)
        numbers=list(word.split())
        for j in range(len(numbers)):
            numbers[j]=int(numbers[j])
        return len(set(numbers))