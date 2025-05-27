"""Given an array arr, the task is to find whether the arr is palindrome or not. If the arr is palindrome then return true else return false.

An array is said to be palindrome if its reverse array matches the original array. 

Examples:

Input: arr = [1, 2, 3, 2, 1]
Output: true
Explanation: Here we can see we have [1, 2, 3, 2, 1] if we reverse it we can find [1, 2, 3, 2, 1] which is the same as before. So, the answer is true.
Input: arr = [1, 2, 3, 4, 5]
Output: false
Explanation: Here we can see we have [1, 2, 3, 4, 5] if we reverse it we find [5, 4, 3, 2, 1] which is the not same as before. So, the answer false."""

                                                            #CODE HERE:-


from typing import List

class Solution:
    def isPerfect(self, arr : List[int]) -> bool:
        a=arr[::-1]
        if(a==arr):
            return True
        else:
            return False