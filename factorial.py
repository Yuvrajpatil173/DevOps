# Function to calculate factorial using a loop
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i  # Multiply the result by each number from 1 to n
    return result

# Get user input
num = int(input("Enter a number: "))

# Ensure the number is non-negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Call the function and display the result
    print(f"The factorial of {num} is {factorial(num)}")
