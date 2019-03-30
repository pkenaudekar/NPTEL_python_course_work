"""
Given a list A of numbers, you have to print those numbers which are not multiples of 3.
Input Format:
The first line contains the numbers of list A separated by a space.
Output Format:
Print the numbers in a single line separated by a space which are not multiples of 3.
Example:
Input:
1 2 3 4 5 6 5
Output:
1 2 4 5 5
Explanation:
Here the elements of A are 1,2,3,4,5,6,5 and since 3,6 are the multiples of 3 hence after removing them the list becomes 1,2,4,5,5.
"""

#CODE:
array = input()
arr = list(map(int,array.split(' ')))
for i in range(len(arr)):
  if(arr[i]%3!=0):
    print(arr[i], end=" ")