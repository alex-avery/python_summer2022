# Python Course - Summer 2022
# Homework 1
# Alex Avery

# import necessary modules 
import random

# create portfolio class
class Portfolio:
    
    # create initializer for portfolio class
    def __init__(self, cash = 0, stock = {}, mutualfund = {}, transactions = []):
        # amount of cash in portfolio
        self.cash = cash
        # stocks and shares in portfolio 
        self.stock = stock
        # mutual funds and shares in portfolio
        self.mutualfund = mutualfund
        # transaction log
        self.transactions = transactions
          
    # create function to add cash
    def addCash(self, amount):
        # amount must be greater than zero 
        if amount <= 0:
            print("Please specify an amount greater than zero to deposit.")
        # add cash amount
        else:
            self.cash += amount
            #add to transaction log 
            self.transactions.append(f"Cash deposit: ${amount}")
    
    # create function to remove cash 
    def withdrawCash(self, amount):
        # amount must be greater than zero
        if amount <= 0:
            print("Please specify an amount greater than zero to withdraw.")
        # remove cash amount 
        else:
            self.cash -= amount
            #add to transaction log
            self.transactions.append(f"Cash withdraw: ${amount}")
    
    #create function to buy stocks 
    def buyStock(self, shares, stock):
        # can only buy stocks worth the amount of cash in portfolio
        stock_total = stock.price * shares
        if stock_total > self.cash:
            print("You do not have enough cash to cover this transaction.")
        else:
            # add stock shares to portfolio 
            self.stock.update({stock.symbol: shares})
            # subtract stock price from cash
            self.cash -= stock_total
            # add to transaction log
            self.transactions.append(f"Bought {shares} shares of {stock.symbol}")
    
    # create function to buy mutual funds
    def buyMutualFund(self, shares, mutualfund):
        mutualfund_total = shares * 1
        if mutualfund_total > self.cash:
            print("You do not have enough cash to cover this transaction.")
        else:
            # add mutual fund shares to portfolio 
            self.mutualfund.update({mutualfund.symbol: shares})
            # subtract mutual funds price from cash
            self.cash -= mutualfund_total
            # add to transaction log
            self.transactions.append(f"Bought {shares} shares of {mutualfund.symbol}")
    
    # create function to sell stocks
    def sellStock(self, stock, shares):
        if shares > self.stock.get(stock.symbol):
            print("You do not have this many shares to sell.")
        else:
            # getting price of share uniformly drawn from [0.5-1.5]
            stock_price = random.uniform(0.5 * stock.price, 1.5 * stock.price)
            # multiplying share price by number of shares
            stock_total = stock_price * shares
            # updating number of shares
            self.stock[stock.symbol] -= shares
            # adding cash from shares to portfolio
            self.cash -= stock_total
            # add to transaction log 
            self.transactions.append(f"Sold {shares} shares of {stock.symbol}")
    
    # create function to sell mutual fund
    def sellMutualFund(self, mutualfund, shares):
        if shares > self.mutualfund.get(mutualfund.symbol):
            print("You do not have this many shares to sell.")
        else:
            # getting price of share uniformly drawn from [0.9-1.2]
            mutualfund_price = random.uniform(0.9, 1.2)
            # multiplying share price by number of shares
            mutualfund_total = mutualfund_price * shares
            # updating number of shares
            self.mutualfund[mutualfund.symbol] -= shares
            # adding cash from shares to portfolio
            self.cash -= mutualfund_total
            # add to transaction log 
            self.transactions.append(f"Sold {shares} shares of {mutualfund.symbol}")
            
    #create print method for portfolio
    def __str__(self):
        return (f"cash: {self.cash} \n stock: {self.stock} \n mutual fund: {self.mutualfund}")
    
    # create history function to return transaction log
    def history(self):
        return self.transactions

    
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
portfolio.buyMutualFund(10.3, mf1) #Buys 10.3 shares of "BRT" (check)
portfolio.buyMutualFund(2, mf2) #Buys 2 shares of "GHT" (check)
print(portfolio) #Prints portfolio
#cash: $140.50
#stock: 5 HFH
#mutual funds: 10.33 BRT
# 2 GHT
portfolio.sellMutualFund(mf1, 3) #Sells 3 shares of BRT
portfolio.sellStock(s, 1) #Sells 1 share of HFH
portfolio.withdrawCash(50) #Removes $50 (check)
portfolio.history() ##Prints a list of all transactions ordered by time
