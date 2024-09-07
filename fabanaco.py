#using iterative  approache.


def fibonacci(n):
    fibonacci_sequence = [0, 1]

    while len(fibonacci_sequence) < n:
            next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_term)

    return(fibonacci_sequence ) 
n=int(input("Enter a number :- "))
print("**** From iterative approache. ****\n ")
print("Fibonacci sequence is \n",fibonacci(n))


# using recursive approache.
 
def fibonacci(n):
    if n==0:
         return 0
    elif n==1:
         return 1
    else:
         return (fibonacci(n-1)+fibonacci(n-2))
n=int(input("\n Enter the Number :- "))
arr=[]
for i in range(n):
    arr.append(fibonacci(i))
print("\n**** From recursive approache. ****\n ")
print("Fibonacci sequence is \n",arr)