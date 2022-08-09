## Fill in the following methods for the class 'Clock'

class Clock:
    def __init__(self, hour, minutes):
        self.minutes = minutes
        self.hour = hour

    ## Print the time
    def __str__(self):
        if len(str(self.minutes)) == 1: 
            return (f"{self.hour}:0{self.minutes}")
        else: 
            return  (f"{self.hour}:{self.minutes}")
    
    ## Add time
    ## Don't return anything
    def __add__(self,minutes):
        #first we need to convert the time to minutes 
        time_minutes = ((self.hour * 60) + self.minutes) 
        #now we can add time 
        added_time = time_minutes + minutes
        #next we need to account for if adding time goes over a day 
        added_time = added_time % (24 * 60)
        #now we need to convert this back to the original format 
        self.hour = added_time // 60
        self.minutes = added_time % 60 
        
    ## Subtract time
    ## Don't return anything
    def __sub__(self,minutes):
        #first we need to convert the time to minutes 
        time_minutes = ((self.hour * 60) + self.minutes) 
        #now we can subtract time 
        added_time = time_minutes - minutes
        #next we need to account for if adding time goes over a day 
        added_time = added_time % (24 * 60)
        #now we need to convert this back to the original format 
        self.hour = added_time // 60
        self.minutes = added_time % 60 

    ## Are two times equal?
    def __eq__(self, other):
        if self.hour == other.hour and self.minutes == other.minutes:
            return True
        else:
            return False
    
    ## Are two times not equal?
    def __ne__(self, other):
        if self.hour != other.hour or self.minutes != other.minutes:
            return True
        else:
            return False

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
print(clock1) # 22:25
