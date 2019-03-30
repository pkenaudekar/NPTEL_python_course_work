"""
A panagram is a sentence containing every 26 letters in the English alphabet. Given a string S, check if it is panagram or not.
Input Format:
The first line contains the sentence S.
Output Format:
Print 'YES' or 'NO' accordingly
Example:
Input:
The quick brown fox jumps over the lazy dog
Output:
YES
"""

#CODE:
s=input()
s=s.lower()
panagram = 'YES'
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in alphabets:
    if s.count(i)==0:
        panagram = 'NO'
        break
print(panagram)  