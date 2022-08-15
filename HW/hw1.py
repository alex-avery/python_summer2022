# Python Course - Summer 2022
# Homework 1
# Alex Avery

# create portfolio class
class Portfolio:
    
    # create initializer for portfolio class
    def __init__(self, cash = 0, stocks = {}):
        # amount of cash in portfolio
        self.cash = cash
        # stocks and shares in portfolio 
        self.stocks = stocks
          
    # create function to add cash
    def addCash(self, amount):
        # amount must be greater than zero 
        if amount <= 0:
            print("Please specify an amount greater than zero to deposit.")
        # add cash amount
        else:
            self.cash += amount
    
    # create function to remove cash 
    def withdrawCash(self, amount):
        # amount must be greater than zero
        if amount <= 0:
            print("Please specify an amount greater than zero to withdraw.")
        # remove cash amount 
        else:
            self.cash -= amount
    
    #create function to buy stocks 
    def buyStock(self, shares, stock):
        # can only buy stocks worth the amount of cash in portfolio
        stock_total = stock.price * shares
        if stock_total > self.cash:
            print("You do not have enough cash to cover this transaction.")
        else:
            # add stock shares to portfolio 
            self.stocks[stock.symbol] = {"shares" : shares}
            # subtract stock price from cash
            self.cash -= stock_total
    
# create Stock class 
class Stock:
    # create initializer for stock class
    def __init__(self, price, symbol):
        # price of stock 
        self.price = price 
        # stock symbol
        self.symbol = symbol


# create Mutual Funds class
class MutualFund:
    # create initializer for mutual fund class
    def __init__(self, symbol):
        # mutual funds symbol
        self.symbol = symbol
    

# REQUIREMENTS:
portfolio = Portfolio() #Creates a new portfolio (check)
portfolio.addCash(300.50) #Adds cash to the portfolio (check)
s = Stock(20, "HFH") #Create Stock with price 20 and symbol "HFH" (check)
portfolio.buyStock(5, s) #Buys 5 shares of stock s (check)
mf1 = MutualFund("BRT") #Create MF with symbol "BRT" (check)
mf2 = MutualFund("GHT") #Create MF with symbol "GHT" (check)
portfolio.buyMutualFund(10.3, mf1) #Buys 10.3 shares of "BRT"
portfolio.buyMutualFund(2, mf2) #Buys 2 shares of "GHT"
print(portfolio) #Prints portfolio
#cash: $140.50
#stock: 5 HFH
#mutual funds: 10.33 BRT
# 2 GHT
portfolio.sellMutualFund("BRT", 3) #Sells 3 shares of BRT
portfolio.sellStock("HFH", 1) #Sells 1 share of HFH
portfolio.withdrawCash(50) #Removes $50
portfolio.history() ##Prints a list of all transactions ordered by time
