"""
Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.
Input Format:
The first line of the input contains an email address.
Output Format:
Print the company name in single line.
Example;
Input:
john@google.com
Output:
google 
"""

#CODE:
a,b = input().split("@")
b,c=b.split(".")
print(b)