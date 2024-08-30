
def average(table:list) -> int | float :
    
    if table:
        output = sum(table)/len(table)
    
        return output
    
    return 0

if __name__ == "__main__":
    print(average([0,1,2,3,4,5,6,7,8,9,10]))
    print(average([]))
