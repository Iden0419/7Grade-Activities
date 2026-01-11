A = input("Team1:")
C = input("Team2:")
Liverpool = 95
Arsnal = 90
Chelsea = 88
Mancity = 90
Tot = 86
Manu = 85
Real_madrid = 92
Barcelona = 93
AT_madrid = 90
Bayern = 91
Leverkusen = 89
Frankfurt = 86
Dortmund = 86
Inter = 87
Ac = 86
Napoli = 88
Juventus = 86
PSG = 88
Newcastle = 89
G = input("Guessing score: ")
if eval(A) > eval(C):
    print("")
    if 3 >= eval(A) - eval(C) >= 1:
        if eval(A) < 89:
            import random

            random_value = random.randint(1, 10)
            if random_value == 1 or random_value == 2 or random_value == 3:
                print("%s won" % A)
                print("1-0")
            elif random_value == 4 or random_value == 5:
                print("%s won" % A)
                print("2-1")
            elif random_value == 6:
                print("Tie")
                print("1-1")
            elif random_value == 7:
                print("Tie")
                print("0-0")
            elif random_value == 8:
                print("%s won" % C)
                print("1-2")
            elif random_value == 9:
                print("%s won" % C)
                print("0-2")
            else:
                print("%s won" % A)
                print("3-1")
        if eval(A) >= 89:
            import random

            random_value = random.randint(1, 10)
            if random_value == 1 or random_value == 2 or random_value == 3:
                print("%s won" % A)
                print("3-2")
            elif random_value == 4 or random_value == 5:
                print("%s won" % C)
                print("2-3")
            elif random_value == 6:
                print("Tie")
                print("2-2")
            elif random_value == 7:
                print("Tie")
                print("3-3")
            elif random_value == 8:
                print("%s won" % A)
                print("2-1")
            elif random_value == 9:
                print("%s won" % A)
                print("1-2")
            else:
                print("%s won" % A)
                print("4-1")
    if 3 < eval(A) - eval(C) <= 5:
        import random

        random_value = random.randint(1, 10)
        if random_value == 1 or random_value == 2 or random_value == 3:
            print("%s won" % A)
            print("3-1")
        elif random_value == 4 or random_value == 5:
            print("%s won" % A)
            print("4-1")
        elif random_value == 6:
            print("Tie")
            print("1-1")
        elif random_value == 7:
            print("%s won" % A)
            print("3-2")
        elif random_value == 8:
            print("%s won" % A)
            print("2-1")
        elif random_value == 9:
            print("%s won" % C)
            print("1-2")
        else:
            print("%s won" % A)
            print("2-0")
    if eval(A) - eval(C) > 5:
        import random

        random_value = random.randint(1, 10)
        if random_value == 1 or random_value == 2 or random_value == 3:
            print("%s won" % A)
            print("4-1")
        elif random_value == 4 or random_value == 5:
            print("%s won" % A)
            print("3-1")
        elif random_value == 6:
            print("Tie")
            print("2-2")
        elif random_value == 7:
            print("%s won" % A)
            print("3-2")
        elif random_value == 8:
            print("%s won" % A)
            print("2-1")
        elif random_value == 9:
            print("%s won" % C)
            print("0-1")
        else:
            print("%s won" % A)
            print("4-0")
if eval(C) > eval(A):
    print("")
    if 3 >= eval(C) - eval(A) >= 1:
        if eval(C) < 89:
            import random

            random_value = random.randint(1, 10)
            if random_value == 1 or random_value == 2 or random_value == 3:
                print("%s won" % C)
                print("1-0")
            elif random_value == 4 or random_value == 5:
                print("%s won" % C)
                print("2-1")
            elif random_value == 6:
                print("Tie")
                print("1-1")
            elif random_value == 7:
                print("Tie")
                print("0-0")
            elif random_value == 8:
                print("%s won" % A)
                print("1-2")
            elif random_value == 9:
                print("%s won" % A)
                print("0-2")
            else:
                print("%s won" % C)
                print("3-1")
        if eval(C) >= 89:
            import random

            random_value = random.randint(1, 10)
            if random_value == 1 or random_value == 2 or random_value == 3:
                print("%s won" % C)
                print("3-2")
            elif random_value == 4 or random_value == 5:
                print("%s won" % A)
                print("3-2")
            elif random_value == 6:
                print("Tie")
                print("2-2")
            elif random_value == 7:
                print("Tie")
                print("3-3")
            elif random_value == 8:
                print("%s won" % C)
                print("2-1")
            elif random_value == 9:
                print("%s won" % C)
                print("1-2")
            else:
                print("%s won" % C)
                print("4-1")
    if 3 < eval(C) - eval(A) <= 5:
        import random

        random_value = random.randint(1, 10)
        if random_value == 1 or random_value == 2 or random_value == 3:
            print("%s won" % C)
            print("3-1")
        elif random_value == 4 or random_value == 5:
            print("%s won" % C)
            print("4-1")
        elif random_value == 6:
            print("Tie")
            print("1-1")
        elif random_value == 7:
            print("%s won" % C)
            print("3-2")
        elif random_value == 8:
            print("%s won" % C)
            print("2-1")
        elif random_value == 9:
            print("%s won" % A)
            print("1-2")
        else:
            print("%s won" % C)
            print("4-0")
    if eval(C) - eval(A) > 5:
        import random

        random_value = random.randint(1, 10)
        if random_value == 1 or random_value == 2 or random_value == 3:
            print("%s won" % C)
            print("4-1")
        elif random_value == 4 or random_value == 5:
            print("%s won" % C)
            print("3-1")
        elif random_value == 6:
            print("Tie")
            print("2-2")
        elif random_value == 7:
            print("%s won" % C)
            print("3-2")
        elif random_value == 8:
            print("%s won" % C)
            print("2-1")
        elif random_value == 9:
            print("%s won" % A)
            print("0-1")
        else:
            print("%s won" % C)
            print("4-0")
if eval(A) == eval(C):
    if eval(A) < 89:
        import random

        random_value = random.randint(1, 10)
        if random_value == 1 or random_value == 2 or random_value == 3:
            print("Tie")
            print("1-1")
        elif random_value == 4 or random_value == 5:
            print("Tie")
            print("2-2")
        elif random_value == 6:
            print("Tie")
            print("0-0")
        elif random_value == 7:
            print("%s won" % C)
            print("0-1")
        elif random_value == 8:
            print("%s won" % A)
            print("2-1")
        elif random_value == 9:
            print("%s won" % C)
            print("1-2")
        else:
            print("%s won" % A)
            print("1-0")
    if eval(A) >= 89:
        import random

        random_value = random.randint(1, 10)
        if random_value == 1 or random_value == 2 or random_value == 3:
            print("Tie")
            print("2-2")
        elif random_value == 4 or random_value == 5:
            print("%s won" % C)
            print("3-2")
        elif random_value == 6:
            print("Tie")
            print("3-3")
        elif random_value == 7:
            print("%s won" % A)
            print("3-2")
        elif random_value == 8:
            print("%s won" % C)
            print("2-1")
        elif random_value == 9:
            print("%s won" % A)
            print("1-2")
        else:
            print("Tie")
            print("1-1")
Agree = input("Do you agree with this?  ")
if Agree == "yes":
    print("Thank you ^^")
elif Agree == "no":
    print("Sorry, I'll try to improve more better.")
else:
    print("I cannot understand it.")

