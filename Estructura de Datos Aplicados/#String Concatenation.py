FirstName = "My First Name is Johan"
namestr = FirstName 
print(namestr)
length = len(namestr)
print("Length of" + namestr + " is " + str(length))
for eachletter in FirstName: print (eachletter)





# Function to check if a number is prime
def is_prime(N):

    if N <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    
    for i in range(2, int(N**0.5) + 1):  # Only check up to the square root of N
        if N % i == 0:
            return False  # If divisible, it's not prime
    
    return True  # If no divisors were found, it's prime


# Test the function
test_number = 29
print(f"Is {test_number} a prime number? {is_prime(test_number)}")

