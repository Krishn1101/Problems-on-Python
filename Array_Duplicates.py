"""Given an array arr of integers, find all the elements that occur more than once in the array.
If no element repeats, return an empty array.

Examples:

Input: arr[] = [2, 3, 1, 2, 3]
Output: [2, 3] 
Explanation: 2 and 3 occur more than once in the given array.
Input: arr[] = [0, 3, 1, 2] 
Output: [] 
Explanation: There is no repeating element in the array, so the output is empty.
Input: arr[] = [2]
Output: [] 
Explanation: There is single element in the array. Therefore output is empty."""

                                    #CODE HERE:-

class Solution:
    def findDuplicates(self, arr):
        arr1=[]
        i,j=0,1
        arr.sort()
        while(j<len(arr)):
            if(arr[i]<arr[j]):
                i+=1
                j+=1
            elif(arr[i]==arr[j]):
                arr1.append(arr[i])
                i+=1
                j+=1
            else:
                j+=1
        return (arr1)