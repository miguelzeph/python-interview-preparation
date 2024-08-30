"""
Right a Factoral function.

As a remidner: factorial(n) = 1*2**3*...n
"""

def factorial(number):
    
    fact = 1
    for n in range(1,number+1):
        fact*= n
    
    return fact

if __name__ == "__main__":
    
    for n in range(0,6):
        print(f"factorial of {n}! = {factorial(n)}")