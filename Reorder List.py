# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return []
        #finding middle node
        slow=head
        fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        #reversing and separating second half of the linked list
        prev=None
        cur=slow.next
        while cur:
            new=cur.next
            cur.next=prev
            prev=cur
            cur=new
        slow.next=None
        #merging in the required order
        head1=head
        head2=prev
        while head2:
            a=head1.next
            head1.next=head2
            head1=head2
            head2=a
        return head