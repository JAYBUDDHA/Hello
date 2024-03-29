import math

def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("7. Factorial")
    

    while True:
        choice = input("Enter choice (1/2/3/4/5/6/7): ")

        if choice in ('1', '2', '3', '4', '5'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
            elif choice == '5':
                print("Result:", power(num1, num2))
        elif choice == "7":
            num = int(input("Enter a number : "))
            print("Result:", math.factorial(num))
        else:
            print("Invalid input")

        next_calculation = input(f"Do you want to perform one more operation? (yes/no): ")
        if next_calculation.upper() != "YES":
            break

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    return math.sqrt(x)

if __name__=="__main__":
    main()
