"""
You are given a string s of lowercase English letters and 
an integer array shifts of the same length. Call the shift() of a letter, 
the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.
Return the final string after all such shifts to s are applied.

Example 1:
Input: s = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation: We start with "abc".
After shifting the first 1 letters of s by 3, we have "dbc".
After shifting the first 2 letters of s by 5, we have "igc".
After shifting the first 3 letters of s by 9, we have "rpl", the answer.

Example 2:
Input: s = "aaa", shifts = [1,2,3]
Output: "gfd"
"""

#Approach #1: Prefix Sum

class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        ans = []
        X = sum(shifts) % 26
        for i, c in enumerate(s):
            index = ord(c) - ord('a')
            ans.append(chr(ord('a') + (index + X) % 26))
            X = (X - shifts[i]) % 26

        return "".join(ans)
    
#Testing

solution = Solution()
test_cases = [
    ("abc", [3,5,9], "rpl"),
    ("aaa", [1,2,3], "gfd")
]

for s, shifts, expected in test_cases:
    result = solution.shiftingLetters(s,shifts)
    print(f"Input: String: {s} and Shifts: {shifts}, Expected: {expected}, Got: {result}, {'Passed' if result == expected else 'Failed'}")