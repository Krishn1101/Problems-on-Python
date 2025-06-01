"""Given an array arr[], check whether it is sorted in non-decreasing order. Return true if it is sorted otherwise false.

Examples:

Input: arr[] = [10, 20, 30, 40, 50]
Output: true
Explanation: The given array is sorted.
Input: arr[] = [90, 80, 100, 70, 40, 30]
Output: false
Explanation: The given array is not sorted."""

                                                    #CODE HERE:-

#User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr) -> bool:
        m=[]
        for i in arr:
            m.append(i)
        m.sort()
        if(m==arr):
            return True
        else:
            return False