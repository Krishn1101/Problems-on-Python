"""Given an array, arr of integers. Your task is to write a program to find the maximum value of ∑arr[i]*i, where i = 0, 1, 2,., n-1. You are allowed to rearrange the elements of the array.
Note: Since the output could be large, print the answer modulo 109+7.

Examples:

Input: arr[] = [5, 3, 2, 4, 1]
Output: 40
Explanation: If we arrange the array as [1, 2, 3, 4, 5] then we can see that the minimum index will multiply with minimum number and maximum index will multiply with maximum number. So, 1*0 + 2*1 + 3*2 + 4*3 + 5*4 = 0+2+6+12+20 = 40 mod(109+7) = 40
Input: arr[] = [1, 2, 3]
Output: 8 
Explanation: If we arrange the array as [1, 2, 3], then the minimum index will multiply with the minimum number and the maximum index will multiply with the maximum number: 1*0 + 2*1 + 3*2 = 0 + 2 + 6 = 8 mod(109+7) = 8.
Input: arr[] = [7, 7, 7, 7]
Output: 42
Explanation: Sorted or unsorted, each element is 7. The sum becomes: 7 ∗ 0 + 7 ∗ 1 + 7 ∗ 2 + 7 ∗ 3 = 0 + 7 + 14 + 21 = 42"""

                                                        #CODE HERE:-

class Solution:
    def maxValue(self, arr): 
        arr.sort()
        sm=0
        for i in range(0,len(arr)):
            ans=arr[i]*i
            sm+=ans
        return (sm%(10**9+7))