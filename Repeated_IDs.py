"""Geek is given a task to select at most 10 employees for a company project. Each employee is represented by a single-digit ID number which is unique for all the selected employees for the project. Geek has a technical problem in his system which printed ID number multiple times. You are given array arr having all printed IDs. Help him to get rid of the repeated IDs.

Examples:

Input: arr[] = [8, 8, 6, 2, 1] 
Output: [8, 6, 2, 1] 
Explanation: 8 is repeated, so takes 8 single time.
Input: arr[] = [7, 6, 7, 4, 2, 7] 
Output: [7, 6, 4, 2] 
Explanation: 7 and 6 are repeated, so take 7 and 6 single time."""

                                                        #CODE HERE:-

class Solution:
    def uniqueId(self, arr):
        arr1 = []
        for i in range(len(arr)):
            if arr[i] not in arr1:
                arr1.append(arr[i])
        return arr1