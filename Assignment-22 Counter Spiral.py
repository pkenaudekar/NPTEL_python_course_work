"""
Given a square matrix, you have to write a program to print it in a counter-clockwise spiral form.
Input Format:
The first line of the input contains an integer number n which represents the number of rows and columns in the matrix.
From the second line contains n rows with each row having n elements separated by a space.
Output Format:
Print the elements in a single line with each element separated by a space
Example:
Input:
4
25 1 29 7
24 20 4 32
16 38 29 1
48 25 21 19
Output:
25 24 16 48 25 21 19 1 32 7 29 1 20 38 29 4
Explanation: 
In the above example, each row, first all the elements of the first column is printed which are 25 24 16 48 after that, remaining elements of the last row is printed which are 25 21 and 19.
After which the remaining elements of the last column is printed which are 1 32 and 7 and so on... 
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