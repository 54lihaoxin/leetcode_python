# Best Time to Buy and Sell Stock
# 
# Say you have an array for which the ith element is the price of a given stock on day i.
# 
# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.


debug = True
debug = False


# from CommonClasses import * # hxl: comment out this line for submission


class Solution:
    
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        
        if prices == None or len(prices) < 2:
            return 0
        
        minPrice = prices[0]
        maxProfit = 0
        
        for i in range(1, len(prices)):
            minPrice = min(minPrice, prices[i])
            maxProfit = max(maxProfit, prices[i] - minPrice)
            
        return maxProfit
        
        