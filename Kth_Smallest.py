"""Given an array arr[] and an integer k where k is smaller than the size of the array,
your task is to find the kth smallest element in the given array.

Follow up: Don't solve it using the inbuilt sort function.

Examples :

Input: arr[] = [7, 10, 4, 3, 20, 15], k = 3
Output: 7
Explanation: 3rd smallest element in the given array is 7.
Input: arr[] = [2, 3, 1, 20, 15], k = 4 
Output: 15
Explanation: 4th smallest element in the given array is 15."""

                                #CODE HERE:-

class Solution:

    def kthSmallest(self, arr,k):
        arr1=[]
        j=0
        for j in range(len(arr)):
            mn=min(arr)
            arr.remove(mn)
            arr1.append(mn)
            j+=1
        return (arr1[k-1])