"""Given a string s as input. Delete the characters at odd indices of the string. Return the final string after deletion of characters at odd indices.

Examples :

Input: s = "Geeks"
Output: "Ges" 
Explanation: Deleted "e" at index 1 and "k" at index 3.
Input: s = "GeeksforGeeks"
Output: "GesoGes"
Explanation: Deleted e, k, f, r, e, k at index 1, 3, 5, 7, 9, 11."""

                                                                #CODE HERE:-

class Solution:
    def delAlternate (ob, S):
        t = ""
        for i in range(len(S)):
            if i%2==0:
                t+=S[i]
        return t