"""You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.

Return the index of the peak element.

Your task is to solve it in O(log(n)) time complexity.

 

Example 1:

Input: arr = [0,1,0]

Output: 1

Example 2:

Input: arr = [0,2,1,0]

Output: 1

Example 3:

Input: arr = [0,10,5,2]

Output: 1"""

                                                            #CODE HERE:-

class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        i = 1
        while(arr[i]>arr[i-1]):
            i+=1
        return i-1