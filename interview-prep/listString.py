# Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
# Output: true


# Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
# Output: false

def arrayStringsAreEqual(word1, word2) -> bool:
    return "".join(word1) == "".join(word2)






print(arrayStringsAreEqual(["ab", "c"],["a", "bc"]))
print(arrayStringsAreEqual(["a", "cb"],["ab", "c"]))

"""
    Best Time to Buy and Sell Stock: You are given an array prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

    Ex1: Input: prices = [7,1,5,3,6,4], Output: Output: 5
                          0,1,2,3,4,5
    because  we Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    
    Ex2: Input: prices = [7,6,4,3,1], Output: 0

"""

def getSmallest(prices):
    """find smallest""" 
    minInt = 1232132
    myindex = 0
    for index in enumerate(prices):
        if prices[index] < minInt:
            minInt = prices[index]
            myindex = index
    return myindex, minInt

# prices[i] - minPrice
def maxProfit(prices):
    maxSum = 0 # get max sum
    minInt = min(prices)
    index = prices.index(minInt)

    for i in prices[index:]:
        current = i - minInt
        if current > maxSum:
            maxSum = current

    # maxSum = [current = i - minInt for i in prices[index:] ]
        
    return maxSum

def maxProfit2(prices):
    minPriceToBuy = 1231232
    maxProfit = 0

    for value in prices:
        if value < minPriceToBuy:
            minPriceToBuy = value
        else:
            maxProfit = max(maxProfit, value - minPriceToBuy)
    return maxProfit








prices= [7,1,5,3,6,4]
print(maxProfit(prices))

print(maxProfit2(prices))
