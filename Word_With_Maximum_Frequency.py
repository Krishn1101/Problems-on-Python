"""You are given a string s that is made up of words separated by spaces. Your task is to find the word with the highest frequency, i.e. it appears the most times in the sentence. If multiple words have maximum frequency, then print the word that occurs first in the sentence.

Examples:

Input: s = "the devil in the sky"
Output: "the 2"
Explanation: The frequency of "the" is 2, so we return "the" and its frequency "2" i.e., "the 2" 
Input: s = "this is not right"
Output: "this 1"
Explanation: Every word has the frequency of "1", so we return "this 1" as this occurs first in the sentence"""

                                                        #CODE HERE:-

class Solution:
    def maximumFrequency(self, s):
        ans = s.split()
        freq = {}
        for i in ans:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        
        mx = 0
        val = 0
        for key,value in freq.items():
            if value>mx:
                mx = value
                val = key
        ans = f"{val} {mx}"
        return ans