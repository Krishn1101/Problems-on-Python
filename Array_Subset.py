"""Given two arrays a[] and b[], your task is to determine whether b[] is a subset of a[].

Examples:

Input: a[] = [11, 7, 1, 13, 21, 3, 7, 3], b[] = [11, 3, 7, 1, 7]
Output: true
Explanation: b[] is a subset of a[]
Input: a[] = [1, 2, 3, 4, 4, 5, 6], b[] = [1, 2, 4]
Output: true
Explanation: b[] is a subset of a[]
Input: a[] = [10, 5, 2, 23, 19], b[] = [19, 5, 3]
Output: false
Explanation: b[] is not a subset of a[]"""

                                        #CODE HERE:-

class Solution:
    def isSubset(self, a, b):
        freq1 = {}
        freq2 = {}
        
        for i in a:
            if i not in freq1:
                freq1[i] = 1
            else:
                freq1[i] += 1
        
        for i in b:
            if i not in freq2:
                freq2[i] = 1
            else:
                freq2[i] += 1
            
        for key,value in freq2.items():
            if key not in freq1.keys():
                return False
            elif(key in freq1.keys()):
                if freq2[key] > freq1[key]:
                    return False
        return True