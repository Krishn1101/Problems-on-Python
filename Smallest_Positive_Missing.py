"""You are given an integer array arr[]. Your task is to find the smallest positive number missing from the array.

Note: Positive number starts from 1. The array can have negative integers too.

Examples:

Input: arr[] = [2, -3, 4, 1, 1, 7]
Output: 3
Explanation: Smallest positive missing number is 3.
Input: arr[] = [5, 3, 2, 5, 1]
Output: 4
Explanation: Smallest positive missing number is 4.
Input: arr[] = [-8, 0, -1, -4, -3]
Output: 1
Explanation: Smallest positive missing number is 1."""

                                                #CODE HERE:-

class Solution:
    
    def missingNumber(self,arr):
        arr.sort()
        count=1
        for i in range(len(arr)):
            if(arr[i]<count):
                i+=1
            elif(arr[i]==count):
                count+=1
        return count
                
                