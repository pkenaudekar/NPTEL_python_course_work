"""
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Input Format:
A sequence of values for D with each value separated by a comma.
Output Format:
Print the sequence of Q values with each value separated by a comma.
Example:
Input:
100,150,180
Output:
18,22,24
"""

#CODE:
import math
D = [int(i) for i in input().split(',')] 
C = 50
H = 30.
Q=[]
for i in range(len(D)):
    Q.append(round(math.sqrt(((2 * C * D[i])/H))))
    
for i in range(len(Q)):
    if(i==len(Q)-1):
        print(Q[i])
    else:
        print(Q[i],end=",")    