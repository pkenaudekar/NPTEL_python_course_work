"""
Given a list A of N distinct integer numbers, you can sort the list by moving an element to the end of the list. Find the minimum number of moves required to sort the list using this method in ascending order. 
Input Format:
The first line of the input contains N distinct integers of list A separated by a space.
Output Format
Print the minimum number of moves required to sort the elements.
Example:
Input:
1 3 2 4 5
Output:
3
Explanation:
In the first move, we move 3 to the end of the list. In the second move, we move 4 to the end of the list, and finally, in the third movement, we move 5 to the end. 
"""

#CODE:
A = [int(i) for i in input().split()] 
N = len(A)
temp=[]
sorted = 0
moves = 0
while(sorted != 1):
    if(all(A[i] <= A[i + 1] for i in range(len(A)-1))):
        break
    for i in range(N-1):
        for j in range(i+1,N):
            if(A[i] > A[j]):
                temp.append(A[i])
                break
                
    min_num=min(temp)
            
    temp.clear()
    A.append(min_num)
    A.remove(min_num)
    moves+=1
    i=0    
        
print(moves)