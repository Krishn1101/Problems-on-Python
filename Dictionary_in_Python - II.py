"""You are now familiar with the dictionary in Python. It's time to dive deeper into the dictionary in Python. How can you use a dictionary to store the frequency of elements in list L. Given below is one method:

for i in L:
     dict[i] = 0

for i in L:
     dict[i] += 1
Now, use this concept to solve a question. Given a list arr[], of positive integers, and an integer sum. The task is to check if any pair exists in the array whose sum is equal to the given sum. If such a pair exists return true, otherwise, return false.

Example:

Input: arr[] = [1, 2, 3, 3, 5], sum = 8 
Output: true
Explanation: Pair with sum 8 is present in the array which is (3, 5).
Input: arr[] = [3, 2, 5], sum = 6 
Output: false
Explanation: No such pair exists in the array."""

                                                                #CODE HERE:-

def pair_sum(dict, arr, sum):
    i,j = 0,1
    while(j!=len(arr)):
        if arr[i] + arr[j] == sum:
            return True
        else:
            j+=1
        if j==len(arr):
            i+=1
            j = i+1
    return False