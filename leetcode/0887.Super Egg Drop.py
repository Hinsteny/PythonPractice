#!/usr/bin/python3
from typing import List


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [1] * (K)
        while dp[K - 1] < N:
            for i in range(K - 1, 0, -1):
                dp[i] = dp[i] + dp[i - 1] + 1
            dp[0] = dp[0] + 1
        return dp[0]


if __name__ == '__main__':
    solution = Solution()
    print(solution.superEggDrop(1, 2))
    print(solution.superEggDrop(2, 6))
    print(solution.superEggDrop(3, 14))
    print(solution.superEggDrop(2, 1))
    print(solution.superEggDrop(2, 2))
    print(solution.superEggDrop(2, 3))
    print(solution.superEggDrop(2, 4))
