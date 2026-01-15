"""Given a string of length N, made up of only uppercase characters 'R' and 'G', where 'R' stands for Red and 'G' stands for Green.Find out the minimum number of characters you need to change to make the whole string of the same colour.

Example 1:

Input:
N=5
S="RGRGR"
Output:
2
Explanation:
We need to change only the 2nd and 
4th(1-index based) characters to 'R', 
so that the whole string becomes 
the same colour.
Example 2:

Input:
N=7
S="GGGGGGR"
Output:
1
Explanation:
We need to change only the last 
character to 'G' to make the string 
same-coloured."""

                                                                #CODE HERE:-

class Solution:
    def RedOrGreen(self,N,S):
        freq = {}
        for i in S:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        if len(freq) == 1:
            return 0
        mn = min(freq.values())
        return mn