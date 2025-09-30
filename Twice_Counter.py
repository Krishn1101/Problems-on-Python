"""Given a list of N words. Count the number of words that appear exactly twice in the list.

Example 1:

Input:
N = 3
list = {Geeks, For, Geeks}
Output: 1
Explanation: 'Geeks' is the only word that 
appears twice. 
Example 2:

Input:
N = 8
list = {Tom, Jerry, Thomas, Tom, Jerry, 
Courage, Tom, Courage}
Output: 2
Explanation: 'Jerry' and 'Courage' are the 
only words that appears twice."""

                                            #CODE HERE:-

class Solution:
    def countWords(self,List, n):
        freq = {}
        cnt = 0
        for i in List:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        
        for i in freq.values():
            if i == 2:
                cnt+=1
        return cnt