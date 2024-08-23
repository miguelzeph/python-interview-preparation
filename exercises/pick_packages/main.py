
def solve(weight_0:int, weight_1:int, weight_2:int)-> int:
    
    # Create vector of all weights
    weights = [weight_0, weight_1, weight_2]
    
    # Get maximum weight
    max_weight = max(weights)
    
    # Get index position
    get_index = weights.index(max_weight)
    
    return get_index
    

if __name__ == "__main__":
    
    lists_input = [
        [300,20,30],
        [1000,10001,20],
        [100,100,200],
        [200,200,200], # any answer is okay
        [1,2,3],
        [0,0,10]
    ]
    
    for input in lists_input:
        
        print(
            solve(input[0], input[1],input[2])
        )
