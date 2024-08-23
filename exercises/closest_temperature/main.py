
def closest_temperature(temperatures:list)-> int:
    
    closest = temperatures[0]
    
    for temp in temperatures:
        
        if (abs(temp) < abs(closest)) or ( (abs(temp) == abs(closest)) and (temp > closest) ):
            closest = temp
    
    return closest

if __name__ == "__main__":
    
    lists_input = [
        [1,2,3,4],
        [-10,10,20,30],
        [-2, 2,-2,5],
        [100,200,300,-450]
    ]
    
    for input in lists_input:
        
        print(closest_temperature(input))
