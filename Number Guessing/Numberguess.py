import random
rand_num = random.randint(1,10)
while True:
    usr_inp = int(input("Enter:"))
    if rand_num > usr_inp:
        print("low")
    elif rand_num < usr_inp:
        print("high")
    else:
        print("you got it")
        inp = input("do you want to play (y/n)?")
        if inp =='n':
            break
        elif inp == 'y':
            rand_num = random.randint(1,10)