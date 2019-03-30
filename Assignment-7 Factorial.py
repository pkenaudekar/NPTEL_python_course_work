"""
Given a number n, you have to print the factorial of this number. To know about factorial please click on this link.
Input Format:
A number n.
Output Format:
Print the factorial of n.
Example:
Input:
4
Output:
24 
"""

#CODE:
fact = int(input())
for i in range(1,fact):
  fact = fact * i

print(fact)