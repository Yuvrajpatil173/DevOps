# Function to calculate factorial
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
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

