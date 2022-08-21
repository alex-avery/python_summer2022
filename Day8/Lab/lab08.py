## Exercise 1
## Write a function using recursion to calculate the greatest common divisor of two numbers

## Helpful link:
## https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
If A = 0 then GCD(A,B)=B, since the GCD(0,B)=B, and we can stop.  
If B = 0 then GCD(A,B)=A, since the GCD(A,0)=A, and we can stop.  
Write A in quotient remainder form (A = B⋅Q + R)

Find GCD(B,R) using the Euclidean Algorithm since GCD(A,B) = GCD(B,R)
def gcd(x, y):
    if x == 0:
        return y 
    elif y == 0:
        return x 
    else:
        floor = x // y
        remaindeer = x % y
        x = y * floor + remainder
        
    


## Problem 2
## Write a function using recursion that returns prime numbers less than 121
## remember, primes are not the product of 
## any two numbers except 1 and the number itself
## hint, "hardcode" 2
def find_primes(me = 121, primes = []):
 
## Problem 3
## Write a function that gives a solution to Tower of Hanoi game
## https://www.mathsisfun.com/games/towerofhanoi.html

Example:
Find the GCD of 270 and 192
A=270, B=192
A ≠0
B ≠0
Use long division to find that 270/192 = 1 with a remainder of 78. We can write this as: 270 = 192 * 1 +78
Find GCD(192,78), since GCD(270,192)=GCD(192,78)
A=192, B=78
A ≠0
B ≠0
Use long division to find that 192/78 = 2 with a remainder of 36. We can write this as:
192 = 78 * 2 + 36
Find GCD(78,36), since GCD(192,78)=GCD(78,36)
A=78, B=36
A ≠0
B ≠0
Use long division to find that 78/36 = 2 with a remainder of 6. We can write this as:
78 = 36 * 2 + 6
Find GCD(36,6), since GCD(78,36)=GCD(36,6)
A=36, B=6
A ≠0
B ≠0
Use long division to find that 36/6 = 6 with a remainder of 0. We can write this as:
36 = 6 * 6 + 0
Find GCD(6,0), since GCD(36,6)=GCD(6,0)
A=6, B=0
A ≠0
B =0, GCD(6,0)=6
So we have shown:
GCD(270,192) = GCD(192,78) = GCD(78,36) = GCD(36,6) = GCD(6,0) = 6
GCD(270,192) = 6