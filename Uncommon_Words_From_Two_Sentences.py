"""A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

 

Example 1:

Input: s1 = "this apple is sweet", s2 = "this apple is sour"

Output: ["sweet","sour"]

Explanation:

The word "sweet" appears only in s1, while the word "sour" appears only in s2.

Example 2:

Input: s1 = "apple apple", s2 = "banana"

Output: ["banana"]"""

                                                    #CODE HERE:-

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        arr = []
        s1 = s1.split(" ")
        s2 = s2.split(" ")
        freq1 = {}
        freq2 = {}
        for i in s1:
            if i not in freq1:
                freq1[i] = 1
            else:
                freq1[i] += 1
        for i in s2:
            if i not in freq2:
                freq2[i] = 1
            else:
                freq2[i] += 1
        for key,value in freq1.items():
            if value == 1 and key not in freq2:
                arr.append(key)
        for key,value in freq2.items():
            if value == 1 and key not in freq1:
                arr.append(key)
        return arr