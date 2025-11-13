"""Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two arrays.

 

Example 1:

Input: words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]
Output: 2
Explanation:
- "leetcode" appears exactly once in each of the two arrays. We count this string.
- "amazing" appears exactly once in each of the two arrays. We count this string.
- "is" appears in each of the two arrays, but there are 2 occurrences of it in words1. We do not count this string.
- "as" appears once in words1, but does not appear in words2. We do not count this string.
Thus, there are 2 strings that appear exactly once in each of the two arrays.
Example 2:

Input: words1 = ["b","bb","bbb"], words2 = ["a","aa","aaa"]
Output: 0
Explanation: There are no strings that appear in each of the two arrays.
Example 3:

Input: words1 = ["a","ab"], words2 = ["a","a","a","ab"]
Output: 1
Explanation: The only string that appears exactly once in each of the two arrays is "ab"."""

                                                        #CODE HERE:-

class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        n = len(words1)
        m = len(words2)
        cnt = 0
        freq1 = {}
        freq2 = {}
        for i in words1:
            if i not in freq1:
                freq1[i] = 1
            else:
                freq1[i] += 1
        for i in words2:
            if i not in freq2:
                freq2[i] = 1
            else:
                freq2[i] += 1
        if n>=m:
            for key,value in freq1.items():
                if key in freq2.keys():
                    if freq1[key] == freq2[key] and freq1[key] == 1:
                        cnt+=1
        else:
            for key,value in freq2.items():
                if key in freq1.keys():
                    if freq2[key] == freq1[key] and freq2[key] == 1:
                        cnt+=1
        return cnt