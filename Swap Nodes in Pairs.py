# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        cur=head.next
        head.next=cur.next
        cur.next=head
        ans=cur
        prev=head
        head=prev.next
        while head and head.next:
            cur=head.next
            head.next=cur.next
            cur.next=head
            prev.next=cur
            prev=head
            head=prev.next
        return ans