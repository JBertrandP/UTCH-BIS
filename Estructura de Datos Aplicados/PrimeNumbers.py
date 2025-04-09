def PrimeNumber(Number):

    if Number <= 1:
        return False 
    
    for divisor in range(2, int(Number**0.5) + 1): 
        if Number % divisor == 0:
            return False 
    
    return True  



test_number = 19
print(f"Is {test_number} a prime number? {PrimeNumber(test_number)}")