"""Given an array arr[] containing strings of names. Your task is to return the longest string. If there are multiple names of the longest size, return the first occurring name.

Examples :

Input: arr[] = ["Geek", "Geeks", "Geeksfor", "GeeksforGeek", "GeeksforGeeks"]
Output: "GeeksforGeeks"
Explanation: name "GeeksforGeeks" has maximum length among all names. 
Input: arr[] = ["Apple", "Mango", "Orange", "Banana"]
Output: "Orange"
Explanation: names "Orange" and "Banana" both have maximum length among all names but Orange comes first so answer will be "Orange"."""

                                                                #CODE HERE:-

class Solution:
    def longest(self, arr):
        mx = len(arr[0])
        idx = 0
        
        for i in range(len(arr)):
            if len(arr[i])>mx:
                mx = len(arr[i])
                idx = i
        return  arr[idx]