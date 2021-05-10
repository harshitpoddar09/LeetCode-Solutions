class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for i in alphabets:
            if i not in sentence:
                return 0
        return 1