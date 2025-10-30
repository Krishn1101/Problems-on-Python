"""Given two arrays arr1 and arr2, representing two numbers such that every element of arrays represents a digit. The task is to find the sum of both the numbers.

Examples:

Input : arr1[] = [1, 2], arr2[] = [2, 1]
Output : 33
Explanation: arr1[]=[1,2] number represented by first array is 12. arr2[] = [2, 1] number represented by second array is 21. Sum = 12 + 21 = 33.
Input : arr1[] = [9, 5, 4, 9], arr2[] = [2, 1, 4] 
Output : 9763 
Explanation : sum of 9549 and 214 is 9763."""

                                                                #CODE HERE:-


class Solution:
    def calc_Sum (self, arr1, arr2) :
        import sys
        s1 = ""
        s2 = ""
        for i in range(len(arr1)):
            s1+=str(arr1[i])
            
        for i in range(len(arr2)):
            s2+=str(arr2[i])
        
        sys.set_int_max_str_digits(5755000)
        ans = int(s1) + int(s2)
        return ans
        