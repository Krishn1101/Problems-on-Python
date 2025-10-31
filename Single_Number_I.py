"""Given an array arr[] of positive integers where every element appears even times except for one. Find that number occurring an odd number of times.

Examples:

Input: arr[] = [1, 1, 2, 2, 2]
Output: 2
Explanation: In the given array all element appear two times except 2 which appears thrice.
Input: arr[] = [8, 8, 7, 7, 6, 6, 1]
Output: 1
Explanation: In the given array all element appear two times except 1 which appears once."""

                                                                #CODE HERE:-

class Solution:
    def getSingle(self,arr):
        freq = {}
        for i in arr:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        for key,value in freq.items():
            if value%2==1:
                return key