from math import sqrt
def isPrime(n) -> bool:
    """
    This function accepts a number n and checks whether it is a
    prime or not
    """
    if n <= 1:
        return False
    
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    
    return True

n = int(input("Enter the number: "))
print(isPrime(n))
