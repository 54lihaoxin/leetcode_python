

debug = False


class Solution:
    
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        else:
            balance = 0
            buyPrice = 0
            sellPrice = 0
            isHoldingStock = False
            for i in range(0, len(prices)):
                if i == 0:
                    if (isHoldingStock == False and 
                        prices[i] < prices[i + 1]):
                        # hxl: buy on first day
                        buyPrice = prices[0]
                        isHoldingStock = True
                        if debug: print 'buy i:', i, 'price:', prices[i]
                elif i == (len(prices) - 1):
                    if isHoldingStock == True:  # and prices[i - 1] < prices[i]:
                        sellPrice = prices[i]
                        balance += sellPrice - buyPrice
                        isHoldingStock = False
                        if debug: print 'sell i:', i, 'price:', prices[i], 'balance:', balance
                else:   # hxl: for any day in the middle
                    if (isHoldingStock == True and 
                        prices[i - 1] <= prices[i] and prices[i] > prices[i + 1]):
                        sellPrice = prices[i]
                        balance += sellPrice - buyPrice
                        isHoldingStock = False
                        if debug: print 'sell i:', i, 'price:', prices[i], 'balance:', balance
                    elif (isHoldingStock == False and 
                          prices[i - 1] >= prices[i] and prices[i] < prices[i + 1]):
                        buyPrice = prices[i]
                        isHoldingStock = True
                        if debug: print 'buy i:', i, 'price:', prices[i]
            return balance
        