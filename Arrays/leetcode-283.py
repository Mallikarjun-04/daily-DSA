'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 10^4
-231 <= nums[i] <= 2^31 - 1
'''

def moveZeroes(nums):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==0:
                    nums[i],nums[j]=nums[j],nums[i]
        return (nums)
nums=list(map(int,input().split()))
print(moveZeroes(nums))