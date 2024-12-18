"""
Write a function that reverses a string. 
The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""

#Approach Two Pointers, Iteration

class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
    
#Approach Two Pointers, Recursion
class Solution2:
    def reverseStringRecursively(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(s, left, right):
            #base:
            if left >= right:
                return

            #reccurence relation
            s[left], s[right] = s[right], s[left]
            helper(s, left + 1, right - 1)

        helper(s, 0, len(s) - 1)
        
    
#Testing
solution = Solution()
solution2 = Solution2()

test_cases = [
    (["h","e","l","l","o"], ["o","l","l","e","h"]),
    (["H","a","n","n","a","h"], ["h","a","n","n","a","H"])
]

print("Iterative Test:", end = "\n" * 2)
for original, expected in test_cases:
    s = original.copy()
    solution.reverseString(s)
    print(f"Input: {original}, Expected: {expected}, Got: {s}, {'Passed' if s == expected else 'Failed'}", end="\n" * 2)

print("Recursive Test:" )
for original, expected in test_cases:
    s = original.copy()
    solution2.reverseStringRecursively(s)
    print(f"Input: {original}, Expected: {expected}, Got: {s}, {'Passed' if s == expected else 'Failed'}", end="\n" * 2)
