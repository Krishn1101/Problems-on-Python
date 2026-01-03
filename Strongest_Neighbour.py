"""You are given an array arr[] consisting of positive integers. Return the maximum of every adjacent pairs in the array.

Examples:

Input: arr[] = [1, 2, 2, 3, 4, 5]
Output: [2, 2, 3, 4, 5]
Explanation: Maximum of arr[0] and arr[1] is 2, that of arr[1] and arr[2] is 2, ... and so on.
Input: arr[] = [5, 5]
Output: [5]
Explanation: We only have two elements so max of 5 and 5 is 5 only."""

                                                            #CODE HERE:-

class Solution:
    def maxAdj(self, arr):
        nums = []
        i,j = 0,1
        while j!=len(arr):
            if arr[i]<arr[j]:
                nums.append(arr[j])
                i+=1
                j+=1
            else:
                nums.append(arr[i])
                i+=1
                j+=1
        return nums