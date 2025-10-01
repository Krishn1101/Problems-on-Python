"""You are given two arrays of size n1 and n2. Your task is to find all the elements that are common to both the arrays and sum them. If there are no common elements the output would be 0.

Note: The arrays may contain duplicate elements. However, you need to sum only unique elements that are common to both arrays and answer may be too large so return it with modulo (109+7) .

 

Example1:

Input:
5 6
1 2 3 4 5
2 3 4 5 6 7
Output: 14
Explanation: Common unique elements in both arrays are 2, 3, 4 and 5 so answer will be 2+3+4+5 = 14
Example2:

Input:
5 6
1 2 2 3 5
3 3 2 2 6 5
Output: 10
Explanation: Common unique elements in both arrays are 2, 3 and 5 so answer will be 2+3+5 = 10"""

                                                        #CODE HERE:-

class Solution:
    def commonSum(self,n1,n2,arr1,arr2):
        arr1 = set(arr1)
        arr2 = set(arr2)
        arr1 = arr1.intersection(arr2)
        return(sum(arr1))%((10**9)+7)