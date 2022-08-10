## Fill in the following methods for the class 'Clock'

class Clock:
    def __init__(self, hour, minutes):
        self.minutes = minutes
        self.hour = hour

    ## Print the time
    def __str__(self):
        return str(self.hour) + ":" + str(self.minutes).zfill(2)
    
    ## Add time
    ## Don't return anything
    def __add__(self,minutes):
        addTime = self.hour*60 + self.minutes + minutes
        
        if addTime > 24*60:
            addTime = addTime - 24*60
        
        else :
            addTime = addTime
        
        self.hour = addTime // 60
        self.minute = addTime % 60
    
    ## Subtract time
    ## Don't return anything
    def __sub__(self,minutes):
        subTime = self.hour*60 + self.minutes - minutes
        
        if subTime > 24*60:
            subTime = subTime - 24*60
        elif subTime < 0:
            subTime = subTime + 24*60
        else :
            subTime = subTime
        
        self.hour = subTime // 60
        self.minute = subTime % 60
    
    ## Are two times equal?
    def __eq__(self, other):
        if self.hour == other.hour and self.minutes == other.minutes:
            return True
        else:
            return False
    
    ## Are two times not equal?
    def __ne__(self, other):
        if self.hour == other.hour and self.minutes == other.minutes:
            return False
        else:
            return True

# You should be able to run these
clock1 = Clock(23, 5)
print(clock1) # 23:05
clock2 = Clock(12, 45)
print(clock2) # 12:45
clock3 = Clock(12, 45)
print(clock3) # 12:45

print(clock1 == clock2) ## False
print(clock1 != clock2) ## True
print(clock2 == clock3) ## True

print("testing addition")
clock1 + 60
print(clock1) # 00:05
print(clock1 == Clock(0, 5)) # True

print("testing subtraction")
clock1 - 100
print(clock1) # 22:45