"""
Given a string S of lowercase letters, remove consecutive vowels from S. After removing, the order of the list should be maintained.
Input Format:
Sentence S in a single line
Output Format:
Print S after removing consecutive vowels
Example:
Input:
your article is in queue
Output:
yor article is in qu
Explanation:
In the first word, 'o' and 'u' are appearing together, hence the second letter 'u' is removed. In the fifth word, 'u', 'e', 'u' and 'e' are appearing together, hence 'e', 'u', 'e' are removed. 
"""

#CODE:
S=input()
output=[]
together = 'NO'
vowels=['a','e','i','o','u']
for i in S:
    if vowels.count(i) > 0 and together == 'NO':
        together = 'YES'
        output.append(i)
    elif vowels.count(i) == 0 and together == 'YES':
        together = 'NO'
        output.append(i)
    elif vowels.count(i) == 0 and together == 'NO':
        output.append(i)
    else:
        continue
print ("".join(output)) 