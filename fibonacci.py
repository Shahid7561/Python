# Fibonacci series 
num = int(input("Enter Number: "))
def fib(num):
    fib_sequence = [0, 1]
    for i in range(2,num):
        next = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next)
    return fib_sequence
print(fib(num))