"""A set is an unordered collection of items where every element is unique and must be immutable, but set is mutable. You cannot access an element of set using indexing or slicing, but you can update the set.

Some important functions in Set in Python:
add(): Adds an element to the set.
clear(): Removes all elements from the set
discard(): Removes an element from the set if present.
remove(): Removes an element from the set. If the element is not present, it raises error.
pop(): Removes and returns an arbitary set element. Raise error if the set is empty.
union(): Returns the union of sets in a new set
update(): Updates the set with the union of itself and others
len(): Return the length of set.
sorted(): Return a new sorted list from elements in the set.
sum(): Return the sum of all elements in the set.

Let's implement some methods through a question. The task is to perform given queries in the Set as given below:
a. i element: Add element i to the set.
b. r element: Remove element r from set.
c. s: Find sum of elements in set.

Examples:

Input: st = [6, 7, 81, 2, 1], i = 3, r = 6
Output: 
1 2 3 6 7 81
1 2 3 7 81 
94
Explanation: After adding 3 set becomes [1, 2, 3, 6, 7, 81], after removing 6 set becomes [1, 2, 3, 7, 81]  and sum of set is 94.
Input: st = [1, 9, 6], i = 78, r = 9
Output: 
1 6 9 78 
1 6 78
85
Explanation: After adding 78 set becomes [1, 6, 9, 78], after removing 9 set becomes [1, 6, 78]  and sum of set is 85."""

                                                            #CODE HERE:-

st = {int(x) for x in input().split()}
i = int(input())
r = int(input())

########### Write your code below ###############
# Insert i in set
st.add(i)
########### Write your code above ###############

# Printing the set
for i in sorted(st):
    print (i, end=' ')
print()

########### Write your code below ###############
# Remove r from set
st.remove(r)
########### Write your code above ###############

# Printing the set
for i in sorted(st):
    print (i, end=' ')
print()

########### Write your code below ###############
sm = sum(st) # Sum of set elements
########### Write your code above ###############

# Print sum of set
print(sm)