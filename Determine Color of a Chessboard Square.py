class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        alpha=['a','b','c','d','e','f','g','h']
        num=['1','2','3','4','5','6','7','8']
        if (alpha.index(coordinates[0])%2==0 and num.index(coordinates[1])%2==0) or (alpha.index(coordinates[0])%2!=0 and num.index(coordinates[1])%2!=0):
            return 0
        return 1