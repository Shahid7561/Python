# Factorial of a number 
num = int(input("Enter number: "))
# def fact(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     return fact

# print(fact(num))
factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)
print(f"The factorial of {num} is {factorial(num)}")