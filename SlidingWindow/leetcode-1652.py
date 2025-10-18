#2__1
'''
@leetcode-1652. Defuse the Bomb
You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.

To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

If k > 0, replace the ith number with the sum of the next k numbers.
If k < 0, replace the ith number with the sum of the previous k numbers.
If k == 0, replace the ith number with 0.
As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!

 

Example 1:

Input: code = [5,7,1,4], k = 3
Output: [12,10,16,13]
Explanation: Each number is replaced by the sum of the next 3 numbers. The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around.
Example 2:

Input: code = [1,2,3,4], k = 0
Output: [0,0,0,0]
Explanation: When k is zero, the numbers are replaced by 0. 
Example 3:

Input: code = [2,4,9,3], k = -2
Output: [12,5,6,13]
Explanation: The decrypted code is [3+9, 2+3, 4+2, 9+4]. Notice that the numbers wrap around again. If k is negative, the sum is of the previous numbers.
 

Constraints:

n == code.length
1 <= n <= 100
1 <= code[i] <= 100
-(n - 1) <= k <= n - 1
'''

'''
Important test cases:

case1:
code = [10,5,7,7,3,2,10,3,6,9,1,6]
k = -4

case2:
code = [10,8,7,7,5,3,9,6]
k = 4
'''

def decrypt(code,k):
        
#brute-force-approach
        
#         ans=code+code
#         for i in range(len(code)):
#             if k>0:
#                 code[i]=sum(ans[(i+1):(i+k+1)])
#             elif k<0:
#                 code[i]=sum(ans[(i+len(code))+k:(i+len(code))])
#             elif k==0:
#                 code[i]=0
#         return (code)
# code=list(map(int,input().split()))
# k=int(input())
# print(decrypt(code,k))


    #sliding-window-approach
        ans=code+code
        temp=0
        res=[]
        if k==0:
            return [0]*len(code)
        elif k>0:
            l=0
            for r in range(len(ans)-1):
                temp+=ans[r]
                if r-l==k:
                    temp-=ans[l]
                    res.append(temp)
                    l+=1
                    if r==len(code)+k-1:
                        break
            return res
        elif k<0:
            l=len(ans)-1
            for r in range(len(ans)-1,-1,-1):
                temp+=ans[r]
                if r-l==k:
                    temp-=ans[l]
                    res.append(temp)
                    l-=1
                    if r==len(code)+k:
                        break
                        
            res.reverse()
            return res
code=list(map(int,input().split()))
k=int(input())
print(decrypt(code,k))
