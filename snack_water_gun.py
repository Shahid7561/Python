# 0 for Snack,1 for Water,2 for Gun
import random
while True:
    comp = random.randint(0,2)
    user_num = int(input("0 for Snack,1 for Water,2 for Gun: "))
    if comp == user_num:
        print(f"computer choose : {comp}")
        print(f"User choose : {user_num}")
        print("MATCH DRAW")
    if comp == 0 and user_num == 1:
        print(f"computer choose : {comp}")
        print(f"User choose : {user_num}")
        print("Computer Win")
    if comp == 0 and user_num == 2:
        print(f"computer choose : {comp}")
        print(f"User choose : {user_num}")
        print("User Win")
    if user_num == 0 and comp == 1:
        print(f"computer choose : {comp}")
        print(f"User choose : {user_num}")
        print("User Win") 
    if user_num == 0 and comp == 2:
        print(f"computer choose : {comp}")
        print(f"User choose : {user_num}")
        print("Computer Win")
    if comp == 1 and user_num == 2:
        print(f"computer choose : {comp}")
        print(f"User choose : {user_num}")
        print("Computer Win") 
    if user_num == 1 and comp == 2:
        print(f"computer choose : {comp}")
        print(f"User choose : {user_num}")
        print("User Win") 