import random
# generating random number
random_num=random.randint(1,100)
# loop 
attempts=0
while True:
# ask the user to write random number
    try:
        user_num=int(input("WRITE THE NUMBER BETWEEN (1-100):-"))
    except ValueError:
        print("PLEASE ENTER VALID NUMBER")
        continue
    attempts=attempts+1
    if user_num>random_num:
        print("TOO HIGH")
    elif user_num<random_num:
        print("TOO LOW")
    else:
        print(f"CONTRAGULATIONS YOU GUESS IT IN {attempts} ATTEMPTS")
        break