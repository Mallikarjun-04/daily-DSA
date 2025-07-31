"""
#leetcode-242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.


Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.

"""

def isAnagram(s,t):
    diki={}
    for i in s:
        if i in diki:
            diki[i]+=1
        else:
            diki[i]=1
    dik={}
    for i in t:
        if i in dik:
            dik[i]+=1
        else:
            dik[i]=1

    return diki==dik
s,t=input().split()
print(isAnagram(s,t))
    
