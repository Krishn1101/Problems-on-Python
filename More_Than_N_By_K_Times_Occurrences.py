"""Given an array arr and an element k. The task is to find the count of elements in the array that appear more than n/k times and n is length of arr.

Examples :

Input: arr = [3, 1, 2, 2, 1, 2, 3, 3], k = 4
Output: 2
Explanation: In the given array, 3 and 2 are the only elements that appears more than n/k times.
Input: arr = [2, 3, 3, 2], k = 3
Output: 2
Explanation: In the given array, 3 and 2 are the only elements that appears more than n/k times. So the count of elements are 2.
Input: arr = [1, 4, 7, 7], k = 2
Output: 0
Explanation: In the given array, no element appears more than n/k times."""

                                                        #CODE HERE:-

class Solution:
    def countOccurence(self,arr, k):
        freq = {}
        n = len(arr)
        cnt = 0
        for i in arr:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        for value in freq.values():
            if value > n/k:
                cnt+=1
        return cnt