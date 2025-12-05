"""Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]"""

                                                #CODE HERE:-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0

        curr = head
        while curr!=None:
            l+=1
            curr = curr.next

        curr = head
        if l == 1:
            return (None)
        elif l == 2:
            if n == 1:
                curr.next = None
                return curr
            elif n == 2:
                return curr.next
        else:
            fast = head
            slow = head
            for i in range(n):
                fast = fast.next

            if fast==None:
                head = head.next
                return head
            while fast.next!=None:
                fast = fast.next
                slow = slow.next
            slow.next = slow.next.next
            return head
