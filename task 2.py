#Calculator
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def calculator():
    print("Basic Calculator")
    print("Operations: +, -, *, /")
    print("Enter 'q' to quit")
    
    while True:
        try:
            # Get user input
            operation = input("\nEnter operation (+, -, *, /) or 'q' to quit: ")
            
            if operation.lower() == 'q':
                print("Calculator closed.")
                break
                
            if operation not in ['+', '-', '*', '/']:
                print("Invalid operation! Please use +, -, *, or /")
                continue
                
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            # Perform calculation based on operation
            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)
                
            print(f"Result: {num1} {operation} {num2} = {result}")
            
        except ValueError as e:
            if str(e) == "Cannot divide by zero!":
                print(e)
            else:
                print("Invalid input! Please enter valid numbers.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    calculator()