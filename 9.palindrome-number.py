#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (57.08%)
# Likes:    12777
# Dislikes: 2745
# Total Accepted:    5M
# Total Submissions: 8.7M
# Testcase Example:  '121'
#
# Given an integer x, return true if x is a palindrome, and false otherwise.
#
#
# Example 1:
#
#
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
#
#
# Example 2:
#
#
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
#
#
# Example 3:
#
#
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a
# palindrome.
#
#
#
# Constraints:
#
#
# -2^31 <= x <= 2^31 - 1
#
#
#
# Follow up: Could you solve it without converting the integer to a string?
#


# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 1
        # O(logn) -- 43%
        # return str(x) == str(x)[::-1]

        # 2
        # O(logn) -- 8%
        # without converting to str

        # get len of x
        # max val of x is 2^31 or 2,147,483,648
        # so 10 digits

        # negative values are never palindromic due to the sign
        # if x < 0:
        #     return False

        # # go check len of the number
        # len_of_x = 1
        # while x // (10**len_of_x) != 0:
        #     len_of_x += 1

        # # check val at each digit is symmetric
        # for idx in range(len_of_x // 2):
        #     complement_idx = len_of_x - idx - 1
        #     val_at_idx = (x // (10**idx)) % 10
        #     val_at_complement_idx = (x // (10**complement_idx)) % 10
        #     if val_at_idx != val_at_complement_idx:
        #         return False

        # return True

        # 3
        # O(logn) -- 39%
        # build the number in reverse, then check they are equal
        # if x < 0:
        #     return False

        # temp = x
        # rev = 0
        # while temp != 0:
        #     digit = temp % 10
        #     rev = rev * 10 + digit
        #     temp //= 10

        # return x == rev

        # 4
        # O(logn) -- 64%
        # same as previous, but check half the number
        if x < 0:
            return False

        # can't be palindromic if it has a leading zero
        if (x != 0) and (x % 10) == 0:
            return False

        rev = 0
        while x > rev:
            digit = x % 10
            rev = rev * 10 + digit
            x //= 10

        return (x == rev) or (x * 10 + digit == rev)


# @lc code=end
