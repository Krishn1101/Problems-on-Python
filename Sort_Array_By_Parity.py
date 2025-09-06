"""Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

 

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
Example 2:

Input: nums = [0]
Output: [0]"""

                                            #CODE HERE:-
#Method 01:-
class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        odd=[]
        even=[]
        for i in range(len(nums)):
            if(nums[i]%2==0):
                even.append(nums[i])
            else:
                odd.append(nums[i])
        even.extend(odd)
        return even
    
#Method 02:-                            To run, Uncomment this code:-
# def sortArrayByParity02():
#     nums = list(map(int,input("Enter the elements of the list: ").split()))
#     start = 0
#     for i in range(len(nums)):
#         if nums[i]%2 == 0:
#             nums[start],nums[i] = nums[i],nums[start]
#             start+=1
#     return nums

# print(sortArrayByParity02())