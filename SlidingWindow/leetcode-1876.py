#1
'''
#leetcode-1876. Substrings of Size Three with Distinct Characters

A string is good if there are no repeated characters.

Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
The only good substring of length 3 is "xyz".
Example 2:

Input: s = "aababcabc"
Output: 4
Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
The good substrings are "abc", "bca", "cab", and "abc".
 

Constraints:

1 <= s.length <= 100
s​​​​​​ consists of lowercase English letters.
'''
def countGoodSubstrings(self, s: str) -> int:
        
        #brute-force-approachBrute

        # ans=[]
        # for i in range(len(s)):
        #     for j in range(i,len(s)):
        #         ans.append(s[i:j+1])
        # count=0
        # for x in ans:
        #     if len(x)==3 and len(x)==len((set(x))):
        #         count+=1
        # return (count)

        l=0
        temp=[]
        count=0
        for r in range(len(s)):
            temp.append(s[r])
            if r-l==3:
                temp.pop(0)
                l+=1
            if r-l+1==3 and len(temp)==len(set(temp)):
                c+=1
        return (count)