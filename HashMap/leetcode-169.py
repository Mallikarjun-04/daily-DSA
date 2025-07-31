"""
@leetcode-169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 10^4
-10^9 <= nums[i] <= 10^9
"""
def majorityElement(nums):
    diki={}
    for i in nums:
        if i in diki:
            diki[i]+=1
        else:
            diki[i]=1
    freq_values=diki.values()
    temp=max(freq_values)
    for i in diki:
        if diki[i]==temp:
            return i
nums=list(map(int,input().split()))
print(majorityElement(nums))