# An exercise 

class Senator():
  def __init__(self, name):
    self.name = name
    self.bills_voted_on = [] ## list of Bill objects

  def __str__(self): 
      return "%s\n%s" %(self.name, self.bills_voted_on) 

  def vote(self, bill, choice):
    #update the bill object--add the senator's name to the the list of yes/no/abstain
    bill.votes[choice].append(self.name)
    #update the senator object--add this bill to the bills this senator has voted on
    self.bills_voted_on.append(bill)
    
    
class Bill():
  def __init__(self, title):
    self.title = title
    self.votes = {"yes" : [], "no" : [], "abstain" : []}
    self.passed = None

  def __str__(self): 
      return self.title 

  def result(self):
    # update and return the "passed" variable to indicate True/False if the bill passed
    if len(self.votes['yes']) > len(self.votes['no']):
      self.passed = 'passed'
    else:
      self.passed = 'failed'
    return self.passed


## should be able to do these things
jane = Senator("Jane")
jack = Senator("Jack")
print(jack)
print(jane)
environment = Bill("Environmental Protection")
print(environment)
jane.vote(environment, "yes")
jack.vote(environment, "no")
environment.result()
print(environment.votes)
print(environment.passed)
print(jack.bills_voted_on[0].passed)


