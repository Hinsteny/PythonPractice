#!/usr/bin/python3
from typing import List


class Solution:
    def maxProfit(self, prices) -> int:
        length = len(prices)
        if 0 == length:
            return 0
        m = 2
        n = length
        dp = [[([0] * (2)) for i in range(m + 1)]for i in range(n + 1)]
        minNumber = -((1 << 31) - 1)
        for x in range(0, n + 1, 1):
            dp[x][0][0] = 0
            dp[x][0][1] = minNumber
        for y in range(1, m + 1, 1):
            dp[0][y][0] = 0
            dp[0][y][1] = minNumber
        for i in range(1, m + 1, 1):
            for j in range(1, length + 1, 1):
                dp[j][i][0] = max(dp[j - 1][i][0], dp[j - 1]
                                  [i][1] + prices[j - 1])
                dp[j][i][1] = max(dp[j - 1][i][1], dp[j - 1]
                                  [i - 1][0] - prices[j - 1])
        return dp[n][m][0]


if __name__ == '__main__':
    solution = Solution()
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    maxProfit = solution.maxProfit(prices)
    print(maxProfit)
    prices = [1, 2, 3, 4, 5]
    maxProfit = solution.maxProfit(prices)
    print(maxProfit)
    prices = [7, 6, 4, 3, 1]
    maxProfit = solution.maxProfit(prices)
    print(maxProfit)
