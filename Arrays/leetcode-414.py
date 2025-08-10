"""
@leetcode-414. Third Maximum Number
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.


Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
 

Constraints:

1 <= nums.length <= 10^4
-2^31 <= nums[i] <= 2^31 - 1
 

Follow up: Can you find an O(n) solution?
..Yeah..
"""

def thirdMax(nums):
    if len(nums)<3:
        return max(nums)
    largest=float('-inf')
    sec_largest=float('-inf')
    t_largest=float('-inf')
    for i in range(len(nums)):
        if nums[i]>largest:
            t_largest=sec_largest
            sec_largest=largest
            largest=nums[i]
        elif nums[i]>sec_largest and nums[i]!=largest:
            t_largest=sec_largest
            sec_largest=nums[i]
        elif nums[i]>t_largest and nums[i]!=largest and nums[i]!=sec_largest:
            t_largest=nums[i]
    return t_largest if t_largest!=float('-inf') else max(nums)
nums=list(map(int,input().split()))
print(thirdMax(nums))