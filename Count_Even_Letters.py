"""You are given a string s consisting of lowercase english letters. Your task is to count how many distinct characters appear an even number of times in the string.

Examples:

Input: s = "abacaba"
Output: 2
Explanation: The frequency of a is 4, b is 2 and c is 1 so there are 2 characters with even frequency.
Input: s = "zzacccz"
Output: 0
Explanation:The frequency of z is 3, a is 1 and c is 3 so there are no characters with even frequency."""

                                                        #CODE HERE:-

class Solution:
    def count(self, s):
        freq = {}
        for i in s:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        
        cnt = 0
        for i in freq.values():
            if i%2==0:
                cnt+=1
        return cnt