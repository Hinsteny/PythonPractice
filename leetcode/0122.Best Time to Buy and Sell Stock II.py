#!/usr/bin/python3
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        for i in range(0, len(prices) - 1, 1):
            if prices[i + 1] > prices[i]:
                maxprofit += prices[i + 1] - prices[i]
        return maxprofit


if __name__ == '__main__':
    solution = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    maxProfit = solution.maxProfit(prices)
    print(maxProfit)
    prices = [1, 2, 3, 4, 5]
    maxProfit = solution.maxProfit(prices)
    print(maxProfit)
    prices = [7, 6, 4, 3, 1]
    maxProfit = solution.maxProfit(prices)
    print(maxProfit)
