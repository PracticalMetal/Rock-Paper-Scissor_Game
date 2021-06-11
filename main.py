from random import randint


p=print
i=input

p("To Player vs Player Press 1".center(120))
p("To Player vs Computer Press 2".center(120))
inp=int(i("Enter \n"))

if inp!=1 and inp!=2:
    print("Invalid input!")


elif inp==1:
    user1=i("Enter username 1: ")
    user2=i("Enter username 2: ")

    user1count=0
    user2count=0

    round=int(i("Enter number of rounds\n"))

    for i in range(1,round+1):
        print(f"{user1} enter your choice")
        turnOfUser1= input("R-Rock      P-paper       S-Scissor\n")
        print("\n")
        print(f"{user2} enter your choice")
        turnOfUser2 = input("R-Rock      P-paper       S-Scissor\n")
        print("\n")


        if turnOfUser1=='R' or turnOfUser1=='r':
            if turnOfUser2=='R' or turnOfUser2=='r':
                print("Match Draw!")
                print("-------------------------------------------------------")

                user1count=user1count+1
                user2count=user2count+1
            elif turnOfUser2== 'P' or turnOfUser2=='p':
                print(f"{user2} won!")
                print("-------------------------------------------------------")
                user2count=user2count+1

            else:
                 print(f"{user1} won!")
                 print("-------------------------------------------------------")

                 user1count = user1count + 1


        elif turnOfUser1=='S' or turnOfUser1=='s':
            if turnOfUser2=='S' or turnOfUser2=='s':
                print("Match Draw!")
                print("-------------------------------------------------------")

                user1count=user1count+1
                user2count=user2count+1
            elif turnOfUser2=='R' or turnOfUser2=='r':
                print(f"{user2} won!")
                print("-------------------------------------------------------")
                user2count=user2count+1

            else:
                 print(f"{user1} won!")
                 print("-------------------------------------------------------")
                 user1count = user1count + 1

        else:
            if turnOfUser2 == 'P' or turnOfUser2 == 'p':
                print("Match Draw!")
                print("-------------------------------------------------------")
                user1count = user1count + 1
                user2count = user2count + 1
            elif turnOfUser2 == 'S' or turnOfUser2 == 's':
                print(f"{user2} won!")
                print("-------------------------------------------------------")
                user2count = user2count + 1

            else:
                print(f"{user1} won!")

                user1count = user1count + 1


    if user1count>user2count:
        print(f"{user1} won {user1count}-{user2count}")
    elif user2count>user1count:
        print(f"{user2} won {user2count}-{user1count}")
    else:
        print(f"Draw {user1count}-{user2count}")
        print("-------------------------------------------------------")








else:

    complist=["R","P","S"]


    user = i("Enter username : ")
    

    usercount = 0
    compcount = 0
    

    round = int(i("Enter number of rounds\n"))

    for i in range(1, round + 1):
        c = randint(0, 2)
        print(f"{user} enter your choice")
        turnOfUser = input("R-Rock      P-paper       S-Scissor\n")
        print("\n")

        

        if turnOfUser == 'R' or turnOfUser == 'r':
            if complist[c] == 'R' or complist[c] == 'r':
                print(f"Computer chose {complist[c]}\n")
                print("Match Draw!")
                print("-------------------------------------------------------")

                usercount = usercount + 1
                compcount = compcount + 1
            elif complist[c] == 'P' or complist[c] == 'p':
                print(f"Computer chose {complist[c]}\n")
                print(f"Computer won!")
                print("-------------------------------------------------------")
                compcount = compcount + 1

            else:
                print(f"Computer chose {complist[c]}\n")
                print(f"{user} won!")

                print("-------------------------------------------------------")

                usercount = usercount + 1


        elif turnOfUser == 'S' or turnOfUser == 's':
            if complist[c] == 'S' or complist[c] == 's':
                print(f"Computer chose {complist[c]}\n")
                print("Match Draw!")
                print("-------------------------------------------------------")

                usercount = usercount + 1
                compcount = compcount + 1
            elif complist[c] == 'R' or complist[c] == 'r':
                print(f"Computer chose {complist[c]}\n")
                print(f"Computer won!")
                print("-------------------------------------------------------")
                compcount = compcount + 1

            else:
                print(f"Computer chose {complist[c]}\n")
                print(f"{user} won!")
                print("-------------------------------------------------------")
                usercount = usercount + 1

        else:
            if complist[c] == 'P' or complist[c] == 'p':

                print(f"Computer chose {complist[c]}\n")
                print("Match Draw!")
                print("-------------------------------------------------------")
                usercount = usercount + 1
                compcount = compcount + 1
            elif complist[c] == 'S' or complist[c] == 's':
                print(f"Computer chose {complist[c]}\n")
                print(f"Computer won!")
                print("-------------------------------------------------------")
                compcount = compcount + 1

            else:
                print(f"Computer chose {complist[c]}\n")
                print(f"{user} won!")
                print("-------------------------------------------------------")

                usercount = usercount + 1

    if usercount > compcount:
        print(f"{user} won {usercount}-{compcount}")
    elif compcount > usercount:
        print(f"Computer won {compcount}-{usercount}")
    else:
        print(f"Draw {usercount}-{compcount}")
        print("-------------------------------------------------------")










