"""Given an array of integers arr[], the task is to find the first equilibrium point in the array.

The equilibrium point in an array is an index (0-based indexing) such that the sum of all elements
before that index is the same as the sum of elements after it. Return -1 if no such point exists. 

Examples:

Input: arr[] = [1, 2, 0, 3]
Output: 2 
Explanation: The sum of left of index 2 is 1 + 2 = 3 and sum on right of index 2 is 3.
Input: arr[] = [1, 1, 1, 1]
Output: -1
Explanation: There is no equilibrium index in the array.
Input: arr[] = [-7, 1, 5, 2, -4, 3, 0]
Output: 3
Explanation: The sum of left of index 3 is -7 + 1 + 5 = -1 and sum on right of index 3 is -4 + 3 + 0 = -1."""

                                                #CODE HERE:-

# User function Template for python3

class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        total_sum = sum(arr)
        left_sum = 0

        for j in range(len(arr)):
            right_sum = total_sum - left_sum - arr[j]

            if left_sum == right_sum:
                return j

            left_sum += arr[j]

        return -1
        
        # j=1
        # while(j!=len(arr)):
        #     arr1=arr[0:j]
        #     arr2=arr[j+1:]
        #     sm_arr1=sum(arr1)
        #     sm_arr2=sum(arr2)
        #     if(sm_arr1!=sm_arr2):
        #         j+=1
        #     elif(sm_arr1==sm_arr2):
        #         return j
        #     else:
        #         return -1
        # return -1