# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        temp_a=headA
        count_a=0
        while headA:
            count_a+=1
            headA=headA.next
        temp_b=headB
        count_b=0
        while headB:
            count_b+=1
            headB=headB.next
        if count_a>count_b:
            while count_a!=count_b:
                count_a-=1
                temp_a=temp_a.next
        else:
            while count_a!=count_b:
                count_b-=1
                temp_b=temp_b.next
        while temp_a:
            if temp_a==temp_b:
                return temp_a
            else:
                temp_a=temp_a.next
                temp_b=temp_b.next
        return None