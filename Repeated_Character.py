"""Given a string consisting of lowercase english alphabets. Find the repeated character present first in the string.

NOTE - If there are no repeating characters return '#'.

Example 1:

Input:
S = "geeksforgeeks"
Output: g
Explanation: g, e, k and s are the repeating
characters. Out of these, g occurs first. 
Example 2:

Input: 
S = "abcde"
Output: -1
Explanation: No repeating character present. (You need to return '#')"""

                                                    #CODE HERE:-

#User function Template for python3

class Solution:
    def firstRep(self, s):
        freq = {}
        
        for i in s:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        
        arr = []
        for key,value in freq.items():
            if value>1:
                arr.append(key)
        if len(arr) == 0:
            return '#'
        
        return arr[0]