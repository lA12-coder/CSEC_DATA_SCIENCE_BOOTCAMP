def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y == 0:
        return "Error: Division By Zero Error!"
    return x/y


def calculator():
    print("==== Calculator====")
    print("Choose the number from the options")
    while (True):
        print("\n1, Add")
        print("2, Subtract")
        print("3, Multiply")
        print("4, Divide")
        print("5, Exit")
        
        choice  = int(input("Enter your choice operation (1-5): "))

        if choice == 5:
            print("Good Bye")
            break
        if choice not in [1,2,3,4]:
            print("Enter the correct number only from (1-5)")
            continue
        
        try:
            num1  = float(input("Enter the first number: "))
            num2  = float(input("Enter the second number: "))
        except ValueError:
            print("Enter a number value")
        
        if choice == 1:
            print(f"Sum : {add(num1,num2)}")
        elif choice == 2:
            print(f"Difference : {subtract(num1,num2)}")
        elif choice == 3:
            print(f"Product: {multiply(num1,num2)}")
        elif choice == 4:
            print(f"Quotient : {divide(num1,num2)}")
            
            
calculator()
            
        
    
        
    
    