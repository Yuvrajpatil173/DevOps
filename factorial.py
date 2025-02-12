# Function to calculate factorial
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1# Function to check if a number is Armstrong
def is_armstrong(number):
    # Convert the number to a string to get the number of digits
    num_str = str(number)
    num_digits = len(num_str)
    
    # Sum the digits raised to the power of num_digits
    sum_of_digits = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum is equal to the original number
    return sum_of_digits == number

# Get user input
num = int(input("Enter a number: "))

# Check and print whether the number is an Armstrong number
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

    else:
        return n * factorial(n - 1)

# Input from user
num = int(input("Enter a number to find its factorial: "))

# Ensure the number is non-negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Calculate and display the factorial
    result = factorial(num)
    print(f"The factorial of {num} is {result}.")

