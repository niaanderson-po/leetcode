"""
You are given an array of characters letters that is sorted in non-decreasing order, and a character target. 
There are at least two different characters in letters.
Return the smallest character in letters that is lexicographically greater than target. 
If such a character does not exist, return the first character in letters.

Example 1:
Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.

Example 2:
Input: letters = ["c","f","j"], target = "c"
Output: "f"
Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.

Example 3:
Input: letters = ["x","x","y","y"], target = "z"
Output: "x"
Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].
"""

#Approach: Binary Search

class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        left, right = 0, len(letters) - 1
    
        while left <= right:
            mid = (left + right) // 2

            if letters[mid] <= target:
                    left = mid + 1  # Search in the right half
            else:
                    right = mid - 1  # Search in the left half
        
        if left == len(letters):
            return letters[0]
        else:
            return letters[left]

#Testing  
 
solution = Solution()
test_cases = [
    (["c","f","j"],"a","c"),
    (["c","f","j"],"c","f"),
    (["x","x","y","y"],"z","x")
]

for letters, target, expected in test_cases:
    result = solution.nextGreatestLetter(letters, target)
    print(f"Input: Letters: {letters} and Target: {target}, Expected: {expected}, Got: {result}, {'Passed' if result == expected else 'Failed'}")