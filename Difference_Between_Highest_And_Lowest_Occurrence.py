"""Given an array, the task is to find the difference between the highest occurrence and lowest occurrence of any number in an array.
Note: If only one type of element is present in the array return 0

Examples:

Input: arr[] = [1, 2, 2]
Output: 1
Explanation:  Lowest occurring element (1) occurs once. Highest occurring element (2) occurs 2 times
Input: arr[] = [7, 8, 4, 5, 4, 1, 1, 7, 7, 2, 5]
Output: 2
Explanation : Lowest occurring element (2) occurs once. Highest occurring element (7) occurs 3 times"""

                                                            #CODE HERE:-

class Solution:
    def findDiff(self, arr):
        freq = {}
        for i in arr:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        mn = min(freq.values())
        mx = max(freq.values())
        if mn == mx:
            return 0
        else:
            return abs(mn-mx)