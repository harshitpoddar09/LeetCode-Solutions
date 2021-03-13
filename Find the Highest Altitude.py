class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude=[0]
        for i in gain:
            altitude.append(altitude[len(altitude)-1]+i)
        return max(altitude)