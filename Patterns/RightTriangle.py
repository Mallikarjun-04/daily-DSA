''''
Print Right Angled Triangle Pattern


Print a mirror image of a right-angled triangle using '*'. See examples for more details.

Input Format
The first line of input contains T - the number of test cases. It's followed by T lines, each line contains a single integer N - the size of the pattern.

Output Format
For each test case, print the test case number as shown, followed by the pattern, separated by a new line.

Constraints
1 <= T <= 100
1 <= N <= 100

Example
Input4
2
1
5
10
OutputCase #1:
 *
**
Case #2:
*
Case #3:
    *
   **
  ***
 ****
*****
Case #4:
         *
        **
       ***
      ****
     *****
    ******
   *******
  ********
 *********
**********

'''
def rightTriangle(n):
    for i in range(0,n+1):
        print(" "*(n-i),end="")
        print("*"*i)
t=int(input())
for i in range(t):
    print("Case #" +str(i+1) + ":",end="")
    n=int(input())
    rightTriangle(n)