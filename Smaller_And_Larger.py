"""Given a sorted array arr and a value target, return an array of size 2. The first value is the number of elements less than or equal to the target, and the second value is the number of elements greater than or equal to the target.

Examples:

Input: arr[] = [1, 2, 8, 10, 11, 12, 19],  target = 0
Output: 0, 7
Explanation: There are no elements less or equal to 0 and 7 elements greater to 0.
Input: arr[] = [1, 5, 8, 12, 12, 12, 19], target = 12
Output: 6, 4
Explanation: There are 6 elements less or equal to 12 and 4 elements greater or equal to 12."""

                                                            #CODE HERE:-

class Solution:
    def getMoreAndLess(self, arr, target):
        sm = 0
        gt = 0
        for i in arr:
            if i < target:
                sm+=1
            elif i > target:
                gt+=1
            else:
                sm+=1
                gt+=1
        return sm,gt