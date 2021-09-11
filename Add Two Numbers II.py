#SUBMISSION 2 - 60ms, 14.3mb
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        h1=l1
        num1=0
        while l1:
            num1=(num1*10)+l1.val
            l1=l1.next
        h2=l2
        num2=0
        while l2:
            num2=(num2*10)+l2.val
            l2=l2.next
        add=num1+num2
        add=str(add)
        l1=ListNode(0)
        ans=l1
        for i in add:
            l1.next=ListNode(i)
            l1=l1.next
        return ans.next

#SUBMISSION 1 - 64ms, 14.4mb 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        h1=l1
        num1=0
        while l1:
            num1=(num1*10)+l1.val
            l1=l1.next
        h2=l2
        num2=0
        while l2:
            num2=(num2*10)+l2.val
            l2=l2.next
        add=num1+num2
        def result(self, head, add, num):
            ans=head
            add=str(add)
            if len(str(add))==len(str(num)):
                for i in add:
                    head.val=int(i)
                    head=head.next
            else:
                i=0
                while head.next:
                    head.val=int(add[i])
                    head=head.next
                    i+=1
                head.val=int(add[i])
                i+=1
                head.next=ListNode(int(add[i]))
            return ans
        if len(str(num1))>=len(str(num2)):
            return result(self,h1,add,num1)
        else:
            return result(self,h2,add,num2)