# Python Course - Summer 2022
# Homework 1
# Alex Avery

# create portfolio class
class Portfolio:
    # create initializer for portfolio class
    def _int_(self):
        self.cash = []
    # create function to add or remove cash
    def Cash(self, amount, transaction_type):
        # only allow positive amounts of cash
        if amount <= 0:
            print("Please specify an amount greater than zero to deposit or withdraw")
        # for deposits:
        elif transaction_type == 'deposit':
            self.cash.append(amount)
        # for withdraws: 
        elif transaaction_type == 'withdraw':
            self.cash.append(-1 * amount)
        # for anything not a deposit or withdraw
        else:
            print("Please specify transaction type as deposit or withdraw")
            
        
        

    
# create Stock class
class Stock:


# create Mutual Funds class
class Mutual_Funds:
    


