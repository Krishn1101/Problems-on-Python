"""Given an array arr of integers which may or may not contain duplicate elements. Your task is to remove duplicate elements.

Examples:

Input: arr[] = [1, 2, 3, 1, 4, 2]
Output: [1, 2, 3, 4]
Explanation: 2 and 1 have more than 1 occurence.
Input: arr[] = [1, 2, 3, 4]
Output: [1, 2, 3, 4]
Explanation: There is no duplicate element."""

                                                    #CODE HERE:-

class Solution:
    def removeDuplicate(self, arr):
        freq = {}
        for i in arr:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        return(freq.keys())