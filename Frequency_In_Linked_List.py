"""Frequency in a Linked List
Difficulty: EasyAccuracy: 80.07%Submissions: 85K+Points: 2
Given a singly linked list and a key, count the number of occurrences of the given key in the linked list.

Examples:

Input: Linked List: 1->2->1->2->1->3->1, key = 1

Output: 4
Explanation: 1 appears 4 times. 
Input: Linked List: 1->2->1->2->1, key = 3

Output: 0
Explanation: 3 appears 0 times."""

                                            #CODE HERE:-

"""  
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""
class Solution:
    def count(self, head, key):
        curr = head
        cnt = 0
        while curr.next!=None:
            if curr.data == key:
                cnt+=1
            curr = curr.next
        if curr.data == key:
            cnt+=1
        return cnt