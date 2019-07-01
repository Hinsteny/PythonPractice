#!/usr/bin/python3
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = (1 << 31) - 1
        maxprofit = 0
        for i in range(len(prices)):
            if prices[i] <= minprice:
                minprice = prices[i]
            elif prices[i] - minprice > maxprofit:
                maxprofit = prices[i] - minprice
        return maxprofit


if __name__ == '__main__':
    solution = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    maxProfit = solution.maxProfit(prices)
    print(maxProfit)
    prices = [7, 6, 4, 3, 1]
    maxProfit = solution.maxProfit(prices)
    print(maxProfit)
