# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left==right:
            return head
        ans=head
        prev=None
        l=1
        while l<left:
            prev=head
            head=head.next
            l+=1
        a=None
        end=head
        while head and l<=right:
            new=head.next
            head.next=a
            a=head
            head=new
            l+=1
        end.next=head
        if left!=1:
            prev.next=a
            return ans
        else:
            return a