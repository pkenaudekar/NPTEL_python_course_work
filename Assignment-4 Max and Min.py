"""
Given a list of numbers, find maximum and minimum in this list.
Input Format:
The first line contains numbers separated by a space.
Output Format:
Print maximum and minimum separated by a space
Example:
Input:
1 2 3 4 5
Output:
5 1 
"""

#CODE:
array = input()
arr = list(map(int,array.split(' ')))
arr.sort()
print(str(arr[len(arr)-1])+" "+str(arr[0]))