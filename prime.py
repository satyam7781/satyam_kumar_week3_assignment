'''Write a program that defines a function to check
whether a number is prime. Use this function in a
script to find all prime numbers within a given
range.'''

#create a function check prime number
def is_prime(n): 
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
#create a function to get prime number for a script
def find_primes(start, end):
   
    primes = [n for n in range(start, end + 1) if is_prime(n)]
    return primes

# Example usage
start = int(input("Enter Starting point \n"))
end = int(input("Enter ending point \n"))
primes = find_primes(start, end)
print(f"Prime numbers between {start} and {end}: {primes}")
