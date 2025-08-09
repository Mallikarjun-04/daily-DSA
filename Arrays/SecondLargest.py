'''
https://www.geeksforgeeks.org/problems/second-largest3735/1

Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element.

Examples:

Input: arr[] = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element of the array is 35 and the second largest element is 34.
Input: arr[] = [10, 5, 10]
Output: 5
Explanation: The largest element of the array is 10 and the second largest element is 5.
Input: arr[] = [10, 10, 10]
Output: -1
Explanation: The largest element of the array is 10 and the second largest element does not exist.
Constraints:
2 ≤ arr.size() ≤ 10^5
1 ≤ arr[i] ≤ 10^5

'''

def getSecondLargest(arr):
        if len(arr)<2:
            return -1
        largest=float('-inf')
        sec_largest=float('-inf')
        for i in range(len(arr)):
            if arr[i]>largest:
                sec_largest=largest
                largest=arr[i]
            elif arr[i]>sec_largest and arr[i]!=largest:
                sec_largest=arr[i]
        return sec_largest if sec_largest!=float('-inf') else -1
arr=list(map(int,input().split()))
print(getSecondLargest(arr))