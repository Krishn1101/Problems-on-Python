"""Given two lists of integers, perform the following operations:

zip(): Combine both lists into one iterable of tuples.

filter(): Filter out all elements in list1 that are less than or equal to 2.

map(): Multiply each element of list1 by 2 using a lambda function.

You need to complete the given program.

Examples:

Input: list1 = [1, 2, 3, 4, 5], list2 = [6, 7, 8, 9, 10]
Output:
[(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
[1, 2]
[2, 4, 6, 8, 10]"""

                        #CODE HERE:-

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

# Use zip() to combine multiple lists into a single iterable  
zipped = zip(list1,list2)
print(list(zipped))   

# Use filter() with lambda function 
# to filter out numbers less than or equal to 2 in list1  
filtered =   filter(lambda x: x<=2, list1)
print(list(filtered))

# Using map() with lambda function 
# to multiply each number of list1 by 2 
mapped = map(lambda x: x*2, list1)
print(list(mapped))
