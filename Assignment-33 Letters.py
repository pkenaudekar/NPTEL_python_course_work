"""
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Input Format:
The first line of the input contains a statement.
Output Format:
Print the number of upper case and lower case respectively separated by a space.
Example:
Input:
Hello world!
Output:
1 9 
"""

#CODE:
S = input()
upper=0
lower=0
for i in S:
    if(i.isupper()):
        upper+=1
    if(i.islower()):
        lower+=1

print(upper,lower)