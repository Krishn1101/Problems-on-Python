"""Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.

You need to solve this problem without utilizing the built-in sort function.

Examples:

Input: arr[] = [0, 1, 2, 0, 1, 2]
Output: [0, 0, 1, 1, 2, 2]
Explanation: 0s 1s and 2s are segregated into ascending order.
Input: arr[] = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
Explanation: 0s 1s and 2s are segregated into ascending order."""

                                    #CODE HERE:-

class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        zero=arr.count(0)
        one=arr.count(1)
        two=arr.count(2)
        arr.clear()
        for i in range(0,zero):
            arr.append(0)
        for j in range(0,one):
            arr.append(1)
        for k in range(0,two):
            arr.append(2)
        return arr