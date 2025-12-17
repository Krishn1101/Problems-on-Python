"""Given an array arr[], find the first repeating element. The element should occur more than once and the index of its first occurrence should be the smallest.

Note:- The position you return should be according to 1-based indexing. 

Examples:

Input: arr[] = [1, 5, 3, 4, 3, 5, 6]
Output: 2
Explanation: 5 appears twice and its first appearance is at index 2 which is less than 3 whose first the occurring index is 3.
Input: arr[] = [1, 2, 3, 4]
Output: -1
Explanation: All elements appear only once so answer is -1."""

                                                            #CODE HERE:-

class Solution:
    def firstRepeated(self,arr):
        freq = {}
        
        for i in arr:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        
        num = []
        for key,value in freq.items():
            if value>1:
                num.append(key)
        
        if len(num) == 0:
            return -1
        
        ans = num[0]
        
        ans = arr.index(ans)
        
        return ans+1