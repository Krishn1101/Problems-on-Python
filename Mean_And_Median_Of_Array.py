"""Given an array of positive integer arr[]. Find the mean and median of the array. 
Where mean is the average value of the given array, median is the average of the two middle elements.

Note: Return the floor value of mean and median.

Examples:

Input: arr[] = [1, 2, 19, 28, 5]
Output: 11 5
Explanation: mean is (1 + 2 + 19  + 28  + 5)/5 = 11.
median is 5 (middle element after sorting)
Input: arr[] = [2, 8, 3, 4]
Output: 4 3
Explanation: mean is floor ((2 + 8 + 3 + 4)/4) = 4.
median is floor ((3 + 4)/2) = 3"""

                                            #CODE HERE:-

class Solution:
    def median(self, arr):
        import numpy as np
        import math
        arr.sort()
        if len(arr)%2==0:
            a = math.floor(np.median(arr))
        else:
            a = math.floor(np.median(arr))
        return a
    def mean(self, arr):
        ans=sum(arr)
        return(ans//len(arr))