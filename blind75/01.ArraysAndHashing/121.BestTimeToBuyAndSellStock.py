"""
Problem: Best Time to Buy and Sell Stock (#121)

Approach:
One-Pass Minimum Price Tracking

Instead of checking every possible buy-sell pair, traverse the array only once.

While traversing:
1. Keep track of the minimum buying price seen so far.
2. If today's price is lower, update the buying price.
3. Otherwise, calculate the profit if sold today.
4. Update the maximum profit whenever a higher profit is found.

Example:
prices = [7, 1, 5, 3, 6, 4]

Price   Buy Price   Profit   Max Profit
---------------------------------------
7       7           0        0
1       1           0        0
5       1           4        4
3       1           2        4
6       1           5        5
4       1           3        5

Final Answer:
Maximum Profit = 5

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def maxProfit(self, prices):
        buy = prices[0]
        profit = 0

        for i in range(1, len(prices)):

            # Found a better minimum buying price
            if prices[i] < buy:
                buy = prices[i]

            # Check profit if sold today
            elif prices[i] - buy > profit:
                profit = prices[i] - buy

        return profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    solution = Solution()

    print("Maximum Profit:", solution.maxProfit(prices))
