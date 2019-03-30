"""
A semiprime number is an integer which can be expressed as a product of two distinct primes. For example 15 = 3*5 is a semiprime number but 9 = 3*3 is not .
Given an integer number N, find whether it can be expressed as a sum of two semi-primes or not (not necessarily distinct).
Input Format:
The first line contains an integer N.
Output Format:
Print 'Yes' if it is possible to represent N as a sum of two semiprimes 'No' otherwise.
Example:
Input:
30
Output:
Yes
Explanation:
N = 30 can be expressed as 15+15 where 15 is a semi-prime number (5*3 = 15)
NOTE: N is less than equal to 200
"""

#CODE:
input = int(input())
if(input <=200):
  lower = 1
  upper = input
  prime = []
  possible = 'No'
  for num in range(lower,upper + 1):
    if num > 1:
      for i in range(2,num):
        if (num % i) == 0:
          break
      else:
        prime.append(int(num))
               
  length = len(prime)
  for i in range(length-1):
    for j in range(length-1):
      for k in range(length-1):
        for l in range(length-1):
          if((prime[i]!=prime[j]) and (prime[k]!=prime[l])):
            if((prime[i]*prime[j])+(prime[k]*prime[l])==input):
              possible = 'Yes'
              break
            else:
              continue
    
  print(possible)  