#SUBMISSION 2 - 824ms 39.4mb
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        length=0
        second=head
        first=head
        while head:
            length+=1
            head=head.next
        if length==1:
            return True
        idx=0
        if length%2==0:           
            while idx<length//2:
                second=second.next
                idx+=1
        else:
            while idx<(length//2)+1:
                second=second.next
                idx+=1
        new=second
        prev=None
        while second.next:
            new=second
            second=second.next
            new.next=prev
            prev=new
        second.next=prev
        while second:
            if first.val!=second.val:
                return 0
            else:
                first=first.next
                second=second.next
        return 1

#SUBMISSION 1 - 788ms 46.9mb
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        return arr==arr[::-1]