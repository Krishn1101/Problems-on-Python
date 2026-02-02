"""You are given an integer array arr of size n+2. All elements of the array are in the range from 1 to n. Also, all elements occur once except two numbers which occur twice. Find the two repeating numbers.
Note: Return the numbers in their order of appearing twice. So, if x and y are repeating numbers, and x's second appearance comes before the second appearance of y, then the order should be (x, y).

Examples:

Input: n = 4, arr[] = [1, 2, 1, 3, 4, 3]
Output: [1, 3]
Explanation: In the given array, 1 and 3 are repeated two times, and as 1's second appearance occurs before 2's second appearance, so the output should be 1 3.
Input: n = 2, arr[] = [1, 2, 2, 1]
Output: [2, 1]
Explanation: In the given array, 1 and 2 are repeated two times and second occurence of 2 comes before 1. So the output is 2 1."""

                                                                    #CODE HERE:-

class Solution:
    def twoRepeated(self, arr):
        freq = {}
        arr1 = []
        for i in arr:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        
        for key,value in freq.items():
            if value == 2:
                arr1.append(key)
        
        cnt1 = 0
        cnt2 = 0
        for i in arr:
            if arr1[0] == i:
                cnt1+=1
            if arr1[1] == i:
                cnt2+=1
            if cnt1 == 2 or cnt2 == 2:
                if cnt1 == 2:
                    return arr1
                elif cnt2 == 2:
                    return arr1[::-1]