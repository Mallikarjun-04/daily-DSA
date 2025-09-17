'''
@leetcode-645. Set Mismatch
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]
 

Constraints:

2 <= nums.length <= 10^4
1 <= nums[i] <= 10^4
'''

def findErrorNums(nums):
        diki={}
        ans=[]
        for i in nums:
            if i not in diki:
                diki[i]=1
            else:
                diki[i]+=1
        for i in diki:
            if diki[i]>1:
                ans.append(i)
                break
        temp=list(set(nums))
        n=len(nums)
        x=((n*(n+1)//2)-sum(temp))
        ans.append(x)
        return ans
nums=list(map(int,input().split()))
print(findErrorNums(nums))
