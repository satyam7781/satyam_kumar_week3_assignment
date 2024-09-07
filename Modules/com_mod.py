
#import created module com_math.py
import com_math 

def factorial(num):
    #calcutating the factorial
    result=com_math.factorial(num)
    print(f"factorial of {num} is {result}")
factorial(5)

def gcd(num1,num2):
    #calculating the gcd
    result=com_math.gcd(num1,num2)
    print(f"The Gcd of {num1} and {num2} is {result}")
gcd(49,35)

def add(num1,num2):
    #calculating the sum
    result=com_math.add(num1,num2)
    print(f"The sum of {num1} and {num2} is {result}")
add(66,55)
    
def sub(num1,num2):
    #calculating the difference
    result=com_math.subtract(num1,num2)
    print(f"The subtract of {num1} and {num2} is {result}")
sub(70,65)

def multiply(num1,num2):
    #calculating the product
    result=com_math.multiply(num1,num2)
    print(f"The product of {num1} and {num2} is {result}")
multiply(55,80)

def divison(num1,num2):
    #calculating the divison
    result=com_math.divison(num1,num2)
    print(f"The divison of {num1} and {num2} is {result}")
divison(90,10)