class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        prev=None
        slot=1
        for i in preorder:
            if i==',':
                slot-=1
                if slot<0:
                    return False
                if prev!='#':
                    slot+=2
            prev=i
        if i!='#':
            slot+=1
        else:
            slot-=1
        return slot==0Verify Preorder Serialization of a Binary Tree