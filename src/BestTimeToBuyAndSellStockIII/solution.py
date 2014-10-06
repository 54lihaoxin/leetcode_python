# Best Time to Buy and Sell Stock III
# 
# Say you have an array for which the ith element is the price of a given stock on day i.
# 
# Design an algorithm to find the maximum profit. You may complete at most two transactions.
# 
# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        
        if prices == None or len(prices) < 2:
            return 0
        
        maxProfitFromFirstDay = [0]
        minPrice = prices[0]
        maxProfit = 0
        
        for i in range(1, len(prices)):
            minPrice = min(minPrice, prices[i])
            maxProfit = max(maxProfit, prices[i] - minPrice)
            maxProfitFromFirstDay.append(maxProfit)
        
        if len(prices) < 4:
            return max(maxProfitFromFirstDay)
        
        if debug: print maxProfitFromFirstDay
        
        i = len(prices) - 1
        maxTwoTransactionProfit = max(maxProfitFromFirstDay)
        maxPrice = prices[-1]
        maxProfit = 0
        
        # hxl: scan backward to look for a potential 2nd transaction that makes better profit
        while i > 1:
            maxPrice = max(maxPrice, prices[i])
            maxProfit = max(maxProfit, maxPrice - prices[i])
            maxTwoTransactionProfit = max(maxTwoTransactionProfit, maxProfitFromFirstDay[i-1] + maxProfit)
            i -= 1
        
        return maxTwoTransactionProfit
