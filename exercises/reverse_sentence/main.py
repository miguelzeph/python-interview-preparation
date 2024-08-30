
# 1 - Write a Python function that receives a string containing a sentence
# 2 - and returns the same sentence, but with each word reversed.
# P.S. The punctuation and spaces should remain in the same place.
import re
def reverse_sentence( sentence:str) -> str:
    
    words = sentence.split()
    
    reversed_sentence = []
    for word in words:
        
        reversed_word = ""
        
        i = 0
        for n, letter in enumerate(word):
            if not letter.isalpha():
                i = n
                
                if word[n-1::-1].isalpha():
                    reversed_word += word[n-1::-1] + letter
                
                # sometimes we can gave more than one punctuation
                # ex: test!!!
                else:
                    reversed_word += letter
        
        if not reversed_word:
            reversed_word += word[::-1]
        
        reversed_sentence.append(reversed_word)
    
    return " ".join(reversed_sentence)
            
        
            
    
if __name__ == "__main__":
    
    result = reverse_sentence("Python, I mean, Python language is cool!!! What do you think about that???")
    
    assert result == "nohtyP, I naem, nohtyP egaugnal si looc!!! tahW od uoy kniht tuoba taht???"
    
    print(result)


    