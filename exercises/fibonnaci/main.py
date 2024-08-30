"""
Right a Fibonnaci sequence.

ex: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34....
"""

def fibonnaci(number:int) -> list:
    
    a = 0
    b = 1
    
    seq = []
    for _ in range(0, number):
        seq.append(a)
        
        c = a + b
        a = b
        b = c
    return seq
        
    

if __name__ == "__main__":
    
    print(fibonnaci(20))