class Solution:
    def minimumBuckets(self, street: str) -> int:
        if (street=='H') or (street[:2]=='HH') or (street[-2:]=='HH') or ('HHH' in street):
            return -1
        return street.count('H')-street.count('H.H')