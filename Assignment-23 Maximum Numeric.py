"""
Given an alphanumeric string S, extract maximum numeric value from that string. All the alphabets are in lower case. Take the maximum consecutive digits as a single number.
Input Format:
The first line contains the string S.
Output Format:
Print the maximum value
Example:
Input:
23dsa43dsa98
Output:
98
Explanation:
There are three integer values present in the string, 23, 43 and 98. Among these, 98 is the maximum. 
"""

#CODE:
n=int(input())
arr=[]
while True:
    try:
        num = input().split()
    except EOFError:
        break
    arr.append(num)

count = n*n
x=0
while(count!=0):
    for i in range(x,(n-x)):
        count-=1
        if(count==0):
            print(arr[i][x])
        else:
            print(arr[i][x],end=" ")
        k=i    
    for j in range(x+1,n-x):
        count-=1
        print(arr[k][j],end=" ")
        l=j
    m=(n-(2+x))
    while(m!=(x-1))and count!=0:
        count-=1
        print(arr[m][l],end=" ")
        m-=1
    
    o=n-(2+x)    
    while(o!=(0+x)) and count!=0:
        count-=1
        print(arr[m+1][o],end=" ")
        o-=1
    x+=1