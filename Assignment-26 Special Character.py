"""
Given a string S, check whether it contains any special character or not. Print 'YES' if it does else 'NO'.
Input Format:
The first line contains the string S
Output Format:
Print 'YES' or 'NO'
Example:
Input:
Hi$my*name
Output:
YES
"""

#CODE:
S=input()
output='NO'
for char in S:
    if not((char >= 'A' and char <='Z') or (char >= 'a' and char <='z') or (char >= '0' and char <='9') or (char ==' ')):
        output='YES'
        break
print(output)    