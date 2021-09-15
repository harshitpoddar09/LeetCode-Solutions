# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        length=0
        h1=head
        h2=head
        ans=head
        while head:
            head=head.next
            length+=1
        idx=1
        while idx<k:
            h1=h1.next
            idx+=1
        idx=0
        while idx<length-k:
            h2=h2.next
            idx+=1
        h1.val,h2.val=h2.val,h1.val
        return ans