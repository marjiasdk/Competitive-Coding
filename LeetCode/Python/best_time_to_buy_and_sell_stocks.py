class Solution:
    def maxProfit(self, prices: "list[int]") -> int:
        max_profit = 0
        min_price = prices[0]
        # iterate through the prices
        for i in range(len(prices)):
            # if the current price is less than the minimum, set it to the minimum
            if prices[i] < min_price:
                min_price = prices[i]
            # if the current price - minimum is greater than the max profit, set it to the max profit
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit

"""
            # example: [7,1,5,3,6,4]
            # min_price = 1
            # max_profit = 0
            # i = 2
            # prices[i] = 5
            # prices[i] - min_price = 5 - 1 = 4
            # max_profit = 4
            # i = 3
            # prices[i] = 3
            # prices[i] - min_price = 3 - 1 = 2
            # max_profit = 4
            # i = 4
            # prices[i] = 6
            # prices[i] - min_price = 6 - 1 = 5
            # max_profit = 5
            # i = 5
            # prices[i] = 4
            # prices[i] - min_price = 4 - 1 = 3
            # max_profit = 5
            # return 5
"""