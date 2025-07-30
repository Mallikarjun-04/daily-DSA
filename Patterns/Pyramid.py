'''
Pyramid Pattern bookmark_borderPrint pyramid pattern using '*'. See the example for more details.

Input Format
The first and only line of input contains a single integer N - the size of the pyramid.

Output Format
For the given integer, print the pyramid pattern.

Constraints
1 <= N <= 50

Example
Input
5
Output
    *
   ***
  *****
 *******
*********

'''
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*((2*i)-1))