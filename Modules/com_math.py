
#creating fuctions for common mathematical operations 

# Function for Addition
def add(num1,num2):
    return num1 + num2

# Function for Subtraction
def subtract(num1,num2):
    return num1 - num2

# Function for multiply
def multiply(num1,num2):
    return num1 * num2

# Function for divison
def divison(num1,num2):
    if num2 == 0:
        return "Error! Division by zero is not allowed."
    else:
        return num1 /num2

# Function for factorial
def factorial(num):
    factoria=1
    for i in range(1,num+1):
        factoria*=i
    return(factoria)

# Function for greatest common divisor
def gcd(a, b):
    result = min(a, b)
    while result:
        if a % result == 0 and b % result == 0:
            break
        result -= 1

    return result


