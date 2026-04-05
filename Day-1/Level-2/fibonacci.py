def fibonacci(n):
    """
    returns the n fibonacci sequence
    """
    x , y = 0 , 1
    
    
    for _ in range(n):
        yield x
        x , y =  y , x+y


n =  int(input("Enter a fibonacci number: "))       
print(list(fibonacci(n)))