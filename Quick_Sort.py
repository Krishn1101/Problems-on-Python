"""Implement Quick Sort, a Divide and Conquer algorithm, to sort an array, arr[] in ascending order.
Given an array arr[], with starting index low and ending index high, complete the functions partition() and quickSort().
Use the last element as the pivot, so that all elements less than or equal to the pivot come before it, and elements greater than the pivot follow it.

Note: low and high are inclusive.

Examples:

Input: arr[] = [4, 1, 3, 9, 7]
Output: [1, 3, 4, 7, 9]
Explanation: After sorting, all elements are arranged in ascending order.
Input: arr[] = [2, 1, 6, 10, 4, 1, 3, 9, 7]
Output: [1, 1, 2, 3, 4, 6, 7, 9, 10]
Explanation: Duplicate elements (1) are retained in sorted order.
Input: arr[] = [5, 5, 5, 5]
Output: [5, 5, 5, 5]
Explanation: All elements are identical, so the array remains unchanged."""

                                                        #CODE HERE:-

class Solution:
    def quickSort(self, arr, low, high):
        #base case:-
        if low>=high:
            return
        
        p = self.partition(arr,low,high)
        
        self.quickSort(arr,low,p-1)
        self.quickSort(arr,p+1,high)

    def partition(self, arr, low, high):
        key = arr[high]
        start = low
        
        for i in range(low,high+1):
            if arr[i]<=key:
                arr[i],arr[start] = arr[start],arr[i]
                start+=1
        
        return start-1
        
    def sortArray(self,arr):
        n = len(arr)
        
        self.quickSort(arr,0,n-1)
        
        return arr