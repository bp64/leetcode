#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#
# https://leetcode.com/problems/happy-number/description/
#
# algorithms
# Easy (56.53%)
# Likes:    10377
# Dislikes: 1458
# Total Accepted:    1.5M
# Total Submissions: 2.7M
# Testcase Example:  '19'
#
# Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
#
#
# Starting with any positive integer, replace the number by the sum of the
# squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it
# loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
#
#
# Return true if n is a happy number, and false if not.
#
#
# Example 1:
#
#
# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
#
#
# Example 2:
#
#
# Input: n = 2
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= n <= 2^31 - 1
#
#
#


# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        # 1
        # O(nm) -- 89%
        # convert n to str, iterate through str
        # run calc on each digit to remake n
        # track what numbers have seen before, if seen False
        # seen = set()
        # while n != 1:
        #     if n in seen:
        #         return False
        #     seen.add(n)

        #     n = str(n)
        #     m = 0
        #     for c in n:
        #         m += int(c) ** 2
        #     n = m
        # return True

        # 2
        # O(log(n)) -- 64%
        # math version
        def sum_of_squared_digits(n: int) -> int:
            sum = 0
            while n > 0:
                sum += (n % 10) ** 2
                n //= 10
            return sum

        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = sum_of_squared_digits(n)
        return True


# @lc code=end
