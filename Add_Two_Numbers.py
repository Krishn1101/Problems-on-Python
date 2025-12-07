"""You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]"""

                                                            #CODE HERE:-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def addTwoNumbers(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = head1
        curr2 = head2

        ans = ListNode(-1)
        carry = 0
        curr3 = ans

        while curr1!=None or curr2!=None:
            total = carry
            carry = 0
            if curr1!=None:
                total+=curr1.val
                curr1=curr1.next
            if curr2!=None:
                total+=curr2.val
                curr2 = curr2.next
            
            if total>9:
                carry = 1
                total-=10

            newNode = ListNode(total)
            curr3.next = newNode
            curr3 = curr3.next

        if carry>0:
            newNode = ListNode(carry)
            curr3.next = newNode
        
        return ans.next