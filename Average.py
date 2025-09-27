"""You are given a list arr that contains integers. You need to return average of the non negative integers.

Examples:

Input: arr = [-12, 8, -7, 6, 12, -9, 14]
Output: avg = 10.0
Explanation: The non negative numbers are 8 6 12 14. The sum is 8+6+12+14 = 40, Average = 40/4 = 10.0
Input: arr = [1, 2, 3]
Output: avg = 2.0
Explanation: The non negative numbers are 1 2 3. The sum is 1+2+3 = 6, Average = 6/3 = 2.0
Input: arr = [5, 0, 0, 0]
Output: avg = 1.25
Explanation: The non negative numbers are 5 0 0 0. The sum is 5+0+0+0 = 5, Average = 5/4 = 1.25"""

                                                #CODE HERE:-

def nonNegativeAverage(arr):
    sm = 0
    cnt = 0
    for i in arr:
        if i>=0:
            sm+=i
            cnt+=1
    return(sm/cnt)