"""Given an array arr[] of integers, calculate the median.

Examples:

Input: arr[] = [90, 100, 78, 89, 67]
Output: 89
Explanation: After sorting the array middle element is the median 
Input: arr[] = [56, 67, 30, 79]
Output: 61.5
Explanation: In case of even number of elements, average of two middle elements is the median. 
Input: arr[] = [1, 2]
Output: 1.5
Explanation: The average of both elements will result in 1.5."""

                            #CODE HERE:-

class Solution:
    def findMedian(self, arr):
        arr.sort()
        l=len(arr)
        i=0
        if(l%2==0):
            i=l//2
            avg = (arr[i-1]+arr[i])/2
            return avg
        else:
            i=l//2
            return arr[i]