"""You are given an array arr[] of integers. You have to construct a singly linked list from the elements of the arr[] and return the head of the linked list.

Examples:

Input: arr[] = [1, 2, 3, 4, 5]
Output: 1 -> 2 -> 3 -> 4 -> 5 
Explanation: Linked list for the given array will be,
      
Input: arr[] = [10, 11, 12, 13, 14]
Output: 10 -> 11 -> 12 -> 13 -> 14
Explanation: Linked list for the given array will be,
"""

                                                                    #CODE HERE:-


# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def arrayToList(self, arr):
        ans = Node(arr[0])
        head = ans
        for i in range(1,len(arr)):
            ans.next = Node(arr[i])
            ans = ans.next
        return head