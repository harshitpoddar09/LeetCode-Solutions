# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        if head.val==val:
            while head and head.val==val:
                prev=head
                head=head.next
                prev.next=None
        temp=head
        while head:
            if head.val==val:
                prev.next=head.next
            else:
                prev=head
            head=head.next
        return temp