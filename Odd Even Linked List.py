# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd=ListNode(0)
        odd1=odd
        even=ListNode(0)
        even1=even
        while head and head.next:
            odd.next=ListNode(head.val)
            odd=odd.next
            head=head.next
            even.next=ListNode(head.val)
            even=even.next
            head=head.next
        if head:
            odd.next=ListNode(head.val)
            odd=odd.next
            head=head.next
        even.next=None
        odd.next=even1.next
        return odd1.next