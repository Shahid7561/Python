# check if number is Prime number or not
num = int(input("Enter Number: "))
# for i in range(2,num):
#     if num % i == 0:
#         print(f"{num} is not prime.")
#         break
#     else:
#         print(f"{num} is prime.")
#         break

# check if number is Prime number or not in one line
# print(["is prime." if num > 1 and all(num % i != 0 for i in range(2,num)) else "is not prime"])

# Print prime number between specific range
print([n for n in range(num+1) if n > 1 and all(n % i != 0 for i in range(2,n))])