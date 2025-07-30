"""Print a hollow diamond pattern using '*'. See examples for more details.

Input Format
The first line of input contains T - the number of test cases. It is followed by T lines, each line contains a single odd integer N - the size of the diamond.

Output Format
For each test case, print the test case number as shown, followed by the diamond pattern, separated by a new line.

Constraints
1 <= T <= 100
3 <= N <= 201

Example
Input4
3
7
5
15

OutputCase #1:
 *
* *
 *
Case #2:
   *
  * *
 *   *
*     *
 *   *
  * *
   *
Case #3:
  *
 * *
*   *
 * *
  *
Case #4:
       *
      * *
     *   *
    *     *
   *       *
  *         *
 *           *
*             *
 *           *
  *         *
   *       *
    *     *
     *   *
      * *
       *

"""
def fun(n):
    
    for i in range(n//2 + 1):
        print(" " * (n//2-i),end="")
        print("*",end="")
        if i>0:
            print(" " * (2*i-1),end="")
            print("*",end="")
        print()
    

    for j in range(n//2-1,-1,-1):
        print(" "*(n//2-j),end="")
        print("*",end="")
        if j>0:
            print(" "*(2*j-1),end="")
            print("*",end="")
        print()
       
t=int(input())
for i in range(t):
    print("Case #"+str(i+1)+":")
    n=int(input())
    fun(n)