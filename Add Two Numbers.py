#SUBMISSION 2 - 72 ms
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1=0
        i=0
        while l1:
            num1+=(l1.val)*(10**i)
            i+=1
            l1=l1.next
        num2=0
        j=0
        while l2:
            num2+=(l2.val)*(10**j)
            j+=1
            l2=l2.next
        res=num1+num2
        head=ListNode(res%10)
        ans=head
        res=res//10
        while res>0:
            head.next=ListNode(res%10)
            head=head.next
            res=res//10
        return ans

#SUBMISSION 1 - 64 ms
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        len1=0
        h1=l1
        while l1:
            len1+=1
            l1=l1.next
        len2=0
        h2=l2
        while l2:
            len2+=1
            l2=l2.next
        prev=None
        if len1>=len2:
            ans=h1
            carry=0
            while h2:
                a=h1.val+h2.val+carry
                if a>=10:
                    carry=1
                else:
                    carry=0
                h1.val=a%10
                prev=h1
                h1=h1.next
                h2=h2.next
            while h1:
                a=h1.val+carry
                if a==10:
                    carry=1
                else:
                    carry=0
                h1.val=a%10
                prev=h1
                h1=h1.next
            if carry==1:
                prev.next=ListNode(1)
            return ans
        else:
            ans=h2
            carry=0
            while h1:
                a=h2.val+h1.val+carry
                if a>=10:
                    carry=1
                else:
                    carry=0
                h2.val=a%10
                prev=h2
                h1=h1.next
                h2=h2.next
            while h2:
                a=h2.val+carry
                if a==10:
                    carry=1
                else:
                    carry=0
                h2.val=a%10
                prev=h2
                h2=h2.next
            if carry==1:
                prev.next=ListNode(1)
            return ans