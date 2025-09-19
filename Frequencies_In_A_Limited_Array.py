"""You are given an array arr[] containing positive integers. The elements in the array arr[] range from  1 to n (where n is the size of the array), and some numbers may be repeated or absent. Your have to count the frequency of all numbers in the range 1 to n and return an array of size n such that result[i] represents the frequency of the number i (1-based indexing).

Examples:

Input: arr[] = [2, 3, 2, 3, 5]
Output: [0, 2, 2, 0, 1]
Explanation: We have: 1 occurring 0 times, 2 occurring 2 times, 3 occurring 2 times, 4 occurring 0 times, and 5 occurring 1 time.
Input: arr[] = [3, 3, 3, 3]
Output: [0, 0, 4, 0]
Explanation: We have: 1 occurring 0 times, 2 occurring 0 times, 3 occurring 4 times, and 4 occurring 0 times.
Input: arr[] = [1]
Output: [1]
Explanation: We have: 1 occurring 1 time, and there are no other numbers between 1 and the size of the array."""

                                                    #CODE HERE:-

class Solution:
    def frequencyCount(self, arr):
        freq1 = {}
        for cnt in arr:
            if cnt not in freq1:
                freq1[cnt] = 1
            else:
                freq1[cnt] += 1
        arr2 = []
        for i in range(1,len(arr)+1):
            if i not in freq1.keys():
                arr2.append(0)
            else:
                arr2.append(freq1[i])
        return arr2