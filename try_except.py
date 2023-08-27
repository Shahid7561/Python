# Exception handling in python

# try:
#     num = int(input("Enter Number: "))
#     for i in range(1,11):
#         print(f"{num} * {i} = {num*i}")
# except:
#     print("Invalid Input!")

# a = [1,2,3]
# try:
#     num = int(input("Enter Number: "))
#     print(a[num])
# except IndexError:
#     print("Index out of range")
# except ValueError:
#     print("Invalid Input!")

# print("Some imp lines of code")


# Raising an error in python
num = int(input("Enter number between 1 to 10: "))

if num < 1 or num > 10:
    raise ValueError("Enter number between 1 to 10")
else:
    print(num)