"""
With a given list L of integers, write a program to print this list L after removing all duplicate values with original order preserved.
Example:
If the input list is
12 24 35 24 88 120 155 88 120 155
Then the output should be
12 24 35 88 120 155
Explanation:
Third, seventh and ninth element of the list L has been removed because it was already present.
Input Format:
In one line take the elements of the list L with each element separated by a space.
Output Format:
Print the elements of the modified list in one line with each element separated by a space.
Example:
Input:
12 24 35 24
Output:
12 24 35
"""

#CODE:
arr = [int(i) for i in input().split()] 
L=[]
i=0
while(i<len(arr)):
    j=0
    present=0
    while(j<i):         
        if arr[i]==arr[j]:
            present=1
        j+=1
    if(present==0):
        L.append(arr[i])
    i+=1   
for i in range(len(L)):
    if(i==len(L)-1):
        print(L[i])
    else:
        print(L[i],end=" ")  