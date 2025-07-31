"""
@leetCode-1207. Unique Number of Occurrences

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.


Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
 

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000

"""
def uniqueOccurrences(arr):
    diki={}
    ans=[]
    for i in arr:
        if i in diki:
            diki[i]+=1
        else:
            diki[i]=1
    freq_values = diki.values() # Get all frequency values
    return len(freq_values) == len(set(freq_values)) # Check if frequency values are unique using a set
arr=list(map(int,input().split()))
print(uniqueOccurrences(arr))

       
              
        