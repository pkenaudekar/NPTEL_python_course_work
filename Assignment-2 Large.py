"""
Given two numbers as input, print the larger number.
Input Format:
The first line of input contains two numbers separated by a space
Output Format:
Print the larger number
Example:
Input:
2 3
Output:
3
"""

#CODE:
a,b = input().split(' ')
if int(a) > int(b): print(a)
else: print(b)