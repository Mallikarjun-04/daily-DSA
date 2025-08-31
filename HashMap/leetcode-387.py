'''
@leetcode-387. First Unique Character in a String
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 
Example 1:

Input: s = "leetcode"

Output: 0

Explanation:

The character 'l' at index 0 is the first character that does not occur at any other index.


Example 2:

Input: s = "loveleetcode"

Output: 2

Example 3:

Input: s = "aabb"

Output: -1

 

Constraints:

1 <= s.length <= 10^5
s consists of only lowercase English letters.
'''

def firstUniqChar(s):
        diki={}
        for i in range(len(s)):
            if s[i] not in diki:
                diki[s[i]]=1
            else:
                diki[s[i]]+=1
        for i in range(len(s)):
            if s[i] in diki and diki[s[i]]==1:
                return i
        else:
            return -1
s=input()
print(firstUniqChar(s))