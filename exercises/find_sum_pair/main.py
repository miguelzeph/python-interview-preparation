"""
Implemente the function find_sum_pair(number, k) which takes as input.

- a list of positive integers (numbers)
- a positive integer (k), representing the target sum

Fro example:
- numbers = [1,5,8,1,2]
- k = 13

Your find_sum_pair function should return a list of two integers containing two different indices of a pair of integers
in  [[param, numbers]] that sums to k. Note that:

- The first index of the list is 0.
- the first integer you return should represent the lower index
- [0,0] should return if no pair is found.
- you can not select twice the same index, so the two indices you return must be different
- if a number can be found twice in the list, and if it is the soluction, you can select them. You will return two different indices, which correspond to two equal numbers
- in the case that there are multiple possible pairs that sum to the target return the pair whose left index is the lowest
- in the case of two pairs having the same left index, favor the pair with the lower right index.

For the above example, the correct return value is [1,2]
"""

def find_sum_pair(numbers:list, k = int) -> list[int]:
    
    pairs = []
        
    # first index of list is 0 (OK)
    for i, number_1 in enumerate(numbers):
        for j, number_2 in enumerate(numbers):
            # index must be different
            if i != j:
                total = number_1 + number_2
                if total == k:
                    pairs.append(sorted([i,j]))
    
    if pairs:
        # the first integer you return should represent the lower index
        return sorted(pairs)[0]
    
    # No pair found
    return [0,0]

if __name__ == "__main__":
    
    numbers = [1,5,8,1,2]
    k = 13
    
    result = find_sum_pair(numbers, k)
    print(result)
    
    
    numbers = [1,5,1,1,2]
    k = 2
    
    result = find_sum_pair(numbers, k)
    print(result)