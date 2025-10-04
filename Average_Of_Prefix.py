"""Given an array arr, find the average or mean of the prefix array at every index.

Examples:

Input: arr[] = [10, 20, 30, 40, 50]
Output: [10, 15, 20, 25, 30] 
Explanation: 10 / 1 = 10, (10 + 20) / 2 = 15, (10 + 20 + 30) / 3 = 20 and so on.
Input: arr[] = [12, 2]
Output: [12, 7]"""

                                    #CODE HERE:-

class Solution:
    def prefixAvg(self, arr):
        arr1 = arr.copy()
        sm = arr[0]
        n = len(arr)
        for i in range(len(arr)-1):
            arr[i] = int(sm/(i+1))
            sm = sm + arr[i+1]
        arr[n-1] = int(sum(arr1)/len(arr))
        return arr